from datetime import UTC, datetime

import pytest

from tinlance_sdea.governance import (
    DataClass,
    RetentionPolicy,
    can_share,
    permitted,
    redact_email,
)
from tinlance_sdea.observability import (
    ENTITY_ID,
    OPPORTUNITY_CREATED,
    SCHEMA_URL,
    SCHEMA_VERSION,
    ObservabilityEvent,
    TraceContext,
)
from tinlance_sdea.policy import PolicyDecision, decide


def test_governance_classification_retention_and_redaction() -> None:
    assert can_share(DataClass.PUBLIC, DataClass.PUBLIC)
    assert can_share(DataClass.INTERNAL, DataClass.RESTRICTED)
    assert not can_share(DataClass.RESTRICTED, DataClass.PUBLIC)
    assert permitted(DataClass.CONFIDENTIAL, DataClass.RESTRICTED)
    assert redact_email("contact user@example.com") == "contact [REDACTED_EMAIL]"
    RetentionPolicy(days=30).validate()
    with pytest.raises(ValueError):
        RetentionPolicy(days=-1).validate()


def test_observability_contracts() -> None:
    event = ObservabilityEvent(
        name=OPPORTUNITY_CREATED,
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        attributes={ENTITY_ID: "org:example"},
    )
    assert event.name == OPPORTUNITY_CREATED
    assert SCHEMA_VERSION == "1.0.0"
    assert SCHEMA_URL.endswith("/1.0.0")
    context = TraceContext(trace_id="t1", span_id="s1")
    assert context.child("s2").trace_id == "t1"
    with pytest.raises(ValueError):
        ObservabilityEvent(
            name="dynamic.123",
            occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        )


def test_policy_decisions_are_bounded_and_non_authoritative() -> None:
    assert decide(confidence=0.9) is PolicyDecision.ELIGIBLE
    assert decide(confidence=0.5) is PolicyDecision.REVIEW
    assert decide(confidence=0.1) is PolicyDecision.INSUFFICIENT_EVIDENCE
    with pytest.raises(ValueError):
        decide(confidence=1.2)
    with pytest.raises(ValueError):
        decide(confidence=0.9, threshold=0.0)
