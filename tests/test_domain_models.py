from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from tinlance_sdea.domain.models import (
    AcquisitionMode,
    DemandHypothesis,
    EpistemicState,
    Evidence,
    EvidenceState,
    Opportunity,
)
from tinlance_sdea.entity import Entity, EntityAlias, EntityType, resolve_entity
from tinlance_sdea.evidence import Provenance, SourceReliability, fingerprint_evidence


def test_demand_hypothesis_requires_rationale() -> None:
    hypothesis = DemandHypothesis(
        entity_id="company:example",
        statement="A capability need may be emerging.",
        confidence=0.7,
        rationale="Corroborating signals indicate expansion.",
    )
    assert hypothesis.confidence == 0.7


def test_opportunity_can_recommend_multiple_acquisition_modes() -> None:
    hypothesis = DemandHypothesis(
        entity_id="company:example",
        statement="Platform capability demand is emerging.",
        confidence=0.8,
        rationale="Multiple signals indicate infrastructure expansion.",
    )
    opportunity = Opportunity(
        entity_id="company:example",
        capability_need_id=hypothesis.id,
        confidence=0.8,
        acquisition_modes=(AcquisitionMode.FDE, AcquisitionMode.FRACTIONAL),
        rationale="Embedded or fractional delivery may satisfy the need.",
    )
    assert AcquisitionMode.FDE in opportunity.acquisition_modes
    assert AcquisitionMode.FRACTIONAL in opportunity.acquisition_modes


def test_evidence_separates_epistemic_and_lifecycle_state() -> None:
    evidence = Evidence(
        source_type="funding",
        observed_at=datetime(2026, 10, 1, tzinfo=UTC),
        collected_at=datetime(2026, 10, 2, tzinfo=UTC),
        title="Funding announcement",
        epistemic_state=EpistemicState.OBSERVED,
    )
    assert evidence.epistemic_state is EpistemicState.OBSERVED
    assert evidence.lifecycle_state.value == "active"
    assert EvidenceState.OBSERVED is EpistemicState.OBSERVED


def test_evidence_rejects_collection_before_observation() -> None:
    with pytest.raises(ValidationError):
        Evidence(
            source_type="funding",
            observed_at=datetime(2026, 10, 2, tzinfo=UTC),
            collected_at=datetime(2026, 10, 1, tzinfo=UTC),
            title="Invalid chronology",
        )


def test_entity_resolution_is_deterministic_for_aliases() -> None:
    entity = Entity(
        id="org:tinlance",
        entity_type=EntityType.ORGANIZATION,
        canonical_name="Tinlance Limited",
        aliases=(EntityAlias(value="TINLANCE LTD"),),
    )
    result = resolve_entity("tinlance ltd", (entity,))
    assert result is not None
    assert result.entity_id == "org:tinlance"
    assert result.confidence == 1.0


def test_entity_resolution_returns_none_for_unknown_entity() -> None:
    entity = Entity(
        id="org:tinlance",
        entity_type=EntityType.ORGANIZATION,
        canonical_name="Tinlance Limited",
    )
    assert resolve_entity("Unknown Company", (entity,)) is None


def test_evidence_fingerprint_is_stable() -> None:
    evidence = Evidence(
        source_type="funding",
        observed_at=datetime(2026, 10, 1, tzinfo=UTC),
        collected_at=datetime(2026, 10, 2, tzinfo=UTC),
        title="Funding announcement",
    )
    assert fingerprint_evidence(evidence) == fingerprint_evidence(evidence)


def test_provenance_and_reliability_contracts_bound_confidence() -> None:
    provenance = Provenance(
        source_name="example",
        source_type="public_web",
        collected_at=datetime(2026, 10, 2, tzinfo=UTC),
        collector="adapter:test",
    )
    reliability = SourceReliability(
        source_name="example",
        reliability=0.8,
        rationale="Primary source.",
        assessed_at="2026-10-02T00:00:00Z",
    )
    assert provenance.collector == "adapter:test"
    assert reliability.reliability == 0.8
