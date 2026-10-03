from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from tinlance_sdea.adapters import AdapterCapability, AdapterHealth, AdapterHealthReport
from tinlance_sdea.capability import Capability, CapabilityMapping
from tinlance_sdea.contracts import SDEAEvent
from tinlance_sdea.domain.models import LifecycleState
from tinlance_sdea.entity import Entity, EntityAlias, EntityIdentifier, EntityType
from tinlance_sdea.evaluation import Adjudication, RegressionCase
from tinlance_sdea.evidence import Provenance, SourceReliability
from tinlance_sdea.governance import DataClass
from tinlance_sdea.integrations._shared import IntegrationContract
from tinlance_sdea.observability import ObservabilityEvent, TraceContext
from tinlance_sdea.opportunity import transition
from tinlance_sdea.outcomes import OutcomeAttribution, OutcomeEvent
from tinlance_sdea.signals import SignalRecord, validate_signal
from tinlance_sdea.temporal import TimeInterval, persistence_count, recency_score


def test_identity_and_evidence_validation_edges() -> None:
    with pytest.raises(ValidationError):
        EntityIdentifier(scheme="domain", value="")
    with pytest.raises(ValidationError):
        EntityAlias(value=" ")
    with pytest.raises(ValidationError):
        Entity(id="", entity_type=EntityType.ORGANIZATION, canonical_name="Example")
    with pytest.raises(ValidationError):
        Entity(
            id="org:example",
            entity_type=EntityType.ORGANIZATION,
            canonical_name="Example",
            identifiers=(
                EntityIdentifier(scheme="domain", value="example.com"),
                EntityIdentifier(scheme="domain", value="example.com"),
            ),
        )


def test_provenance_and_reliability_reject_bad_metadata() -> None:
    with pytest.raises(ValidationError):
        Provenance(
            source_name=" ",
            source_type="web",
            collected_at=datetime(2026, 10, 1),
            collector="test",
        )
    with pytest.raises(ValidationError):
        SourceReliability(
            source_name="source",
            reliability=0.5,
            rationale=" ",
            assessed_at=datetime(2026, 10, 1),
        )


def test_signal_validation_edges() -> None:
    signal = SignalRecord(
        entity_id="org:example",
        signal_type="hiring",
        source_event_id="evt",
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        evidence_ids=(uuid4(),),
    )
    assert validate_signal(signal) is signal
    with pytest.raises(ValueError):
        validate_signal(signal.model_copy(update={"signal_type": "unknown"}))
    with pytest.raises(ValidationError):
        SignalRecord(
            entity_id=" ",
            signal_type="hiring",
            source_event_id="evt",
            occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
            observed_at=datetime(2026, 10, 2, tzinfo=UTC),
            evidence_ids=(uuid4(),),
        )


def test_adapter_contract_edges() -> None:
    with pytest.raises(ValidationError):
        AdapterCapability(adapter_name="a", version="1.0.0", max_batch_size=0)
    with pytest.raises(ValidationError):
        AdapterHealthReport(
            adapter_name="a",
            status=AdapterHealth.HEALTHY,
            checked_at=datetime(2026, 10, 1),
        )


def test_temporal_and_observability_edges() -> None:
    with pytest.raises(ValueError):
        TimeInterval(start=datetime(2026, 10, 1), end=datetime(2026, 10, 2))
    with pytest.raises(ValueError):
        persistence_count((datetime(2026, 10, 1),))
    with pytest.raises(ValueError):
        recency_score(
            observed_at=datetime(2026, 10, 1),
            now=datetime(2026, 10, 2),
            half_life_days=7,
        )
    with pytest.raises(ValueError):
        ObservabilityEvent(
            name="opportunity.created",
            occurred_at=datetime(2026, 10, 1),
        )
    with pytest.raises(ValueError):
        TraceContext(trace_id="", span_id="span")


def test_contract_capability_and_outcome_edges() -> None:
    with pytest.raises(ValueError):
        IntegrationContract(consumer="", purpose="test")
    with pytest.raises(ValidationError):
        SDEAEvent(
            event_name="event.created",
            occurred_at=datetime(2026, 10, 1),
            entity_id="org:example",
        )
    with pytest.raises(ValidationError):
        Capability(id="cap", name="Capability", version="1.0.0", aliases=(" ",))
    with pytest.raises(ValidationError):
        CapabilityMapping(source="", capability_id="cap", confidence=0.5, rationale="x")
    with pytest.raises(ValidationError):
        OutcomeEvent(
            id=uuid4(),
            opportunity_id=uuid4(),
            event_type="accepted",
            occurred_at=datetime(2026, 10, 1),
        )
    with pytest.raises(ValidationError):
        OutcomeAttribution(
            opportunity_id=uuid4(),
            outcome_event_id=uuid4(),
            attributed=True,
            confidence=0.5,
            rationale=" ",
        )


def test_evaluation_and_lifecycle_edges() -> None:
    with pytest.raises(ValidationError):
        RegressionCase(case_id="", expected="x", observed="x")
    with pytest.raises(ValidationError):
        Adjudication(case_id="case", decision="", reviewer="human", confidence=0.5)
    retracted = transition(LifecycleState.SUPERSEDED, LifecycleState.RETRACTED)
    assert retracted is LifecycleState.RETRACTED
    with pytest.raises(ValueError):
        transition(LifecycleState.RETRACTED, LifecycleState.ACTIVE)


def test_governance_lattice_is_monotonic() -> None:
    assert DataClass.RESTRICTED != DataClass.PUBLIC


def test_opportunity_record_and_handoff_invariants() -> None:
    from tinlance_sdea.opportunity.models import OpportunityHandoff, OpportunityRecord

    evidence_id = uuid4()
    record = OpportunityRecord(
        id=uuid4(),
        entity_id="org:example",
        capability_id="platform",
        confidence=0.8,
        evidence_ids=(evidence_id,),
        rationale="Evidence-backed opportunity.",
    )
    handoff = OpportunityHandoff(
        opportunity_id=uuid4(),
        entity_id="org:example",
        capability_id="platform",
        confidence=0.8,
        evidence_ids=(evidence_id,),
        rationale="Evidence-backed handoff.",
    )
    assert record.evidence_ids == handoff.evidence_ids
    with pytest.raises(ValidationError):
        OpportunityRecord(
            id=uuid4(),
            entity_id="org:example",
            capability_id="platform",
            confidence=0.8,
            evidence_ids=(),
            rationale="missing",
        )
    with pytest.raises(ValidationError):
        OpportunityHandoff(
            opportunity_id=uuid4(),
            entity_id="org:example",
            capability_id="platform",
            confidence=0.8,
            evidence_ids=(),
            rationale="missing",
        )


def test_integration_and_trace_edge_cases() -> None:
    with pytest.raises(ValidationError):
        IntegrationContract(
            consumer="consumer",
            purpose="purpose",
            allowed_actions=("write", "write"),
        )
    with pytest.raises(ValueError):
        TraceContext(trace_id="trace", span_id="span").child(" ")


def test_temporal_decay_and_reliability_edges() -> None:
    from tinlance_sdea.temporal import decay_score

    with pytest.raises(ValueError):
        decay_score(age_days=-1, half_life_days=7)
    with pytest.raises(ValueError):
        SourceReliability(
            source_name="source",
            reliability=0.5,
            rationale="valid",
            assessed_at=datetime(2026, 10, 1),
        )
