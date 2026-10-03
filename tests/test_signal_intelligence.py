from datetime import UTC, datetime
from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError

from tinlance_sdea.adapters import AdapterCapability, AdapterRegistry, SignalAdapter
from tinlance_sdea.signals import (
    SignalRecord,
    SignalRegistry,
    SignalType,
    deduplicate_signals,
    fingerprint_signal,
    normalize_signal,
    validate_signal,
)


def make_signal(*, source_event_id: str = "evt-1") -> SignalRecord:
    return normalize_signal(
        entity_id="org:example",
        signal_type=SignalType.HIRING,
        source_event_id=source_event_id,
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        evidence_ids=(uuid4(),),
        attributes={"role": "platform engineer", "count": 3},
    )


def test_normalization_is_deterministic_and_typed() -> None:
    signal = make_signal()
    assert signal.signal_type == "hiring"
    assert signal.attributes == {"role": "platform engineer", "count": "3"}
    assert validate_signal(signal) == signal
    assert fingerprint_signal(signal) == fingerprint_signal(signal)


def test_signal_requires_evidence_and_valid_chronology() -> None:
    with pytest.raises(ValidationError):
        SignalRecord(
            entity_id="org:example",
            signal_type="hiring",
            source_event_id="evt-1",
            occurred_at=datetime(2026, 10, 2, tzinfo=UTC),
            observed_at=datetime(2026, 10, 1, tzinfo=UTC),
            evidence_ids=(uuid4(),),
        )
    with pytest.raises(ValidationError):
        SignalRecord(
            entity_id="org:example",
            signal_type="hiring",
            source_event_id="evt-1",
            occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
            observed_at=datetime(2026, 10, 2, tzinfo=UTC),
            evidence_ids=(),
        )


def test_deduplication_keeps_first_occurrence() -> None:
    first = make_signal()
    duplicate = make_signal()
    unique = make_signal(source_event_id="evt-2")
    result = deduplicate_signals((first, duplicate, unique))
    assert len(result) == 2
    assert result[0].id == first.id
    assert result[0].fingerprint is not None


def test_signal_registry_rejects_unknown_type() -> None:
    registry = SignalRegistry()
    assert registry.get("hiring") is SignalType.HIRING
    with pytest.raises(ValueError):
        registry.get("not-a-signal")


class ExampleAdapter(SignalAdapter):
    name = "example"
    source_types = frozenset({"job_board"})

    def normalize(self, payload: dict[str, object]) -> tuple[SignalRecord, ...]:
        return (make_signal(source_event_id=str(payload["id"])),)


def test_adapter_registry_is_explicit_and_capability_is_bounded() -> None:
    registry = AdapterRegistry()
    adapter = ExampleAdapter()
    registry.register(adapter)
    assert registry.get("example") is adapter
    assert adapter.supports("job_board")
    assert not adapter.supports("funding")
    with pytest.raises(ValueError):
        registry.register(adapter)
    capability = AdapterCapability(
        adapter_name="example",
        source_types=frozenset({"job_board"}),
        version="1.0.0",
    )
    assert capability.max_batch_size == 100


def test_signal_fingerprint_changes_when_source_event_changes() -> None:
    assert fingerprint_signal(make_signal(source_event_id="evt-a")) != fingerprint_signal(
        make_signal(source_event_id="evt-b")
    )
