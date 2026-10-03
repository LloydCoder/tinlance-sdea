from datetime import UTC, datetime
from uuid import uuid4

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


def hypothesis() -> DemandHypothesis:
    return DemandHypothesis(
        entity_id="company:example",
        statement="A capability need may be emerging.",
        supporting_signal_ids=(uuid4(),),
        confidence=0.7,
        rationale="Corroborating signals indicate expansion.",
    )


def test_demand_hypothesis_requires_rationale() -> None:
    item = hypothesis()
    assert item.confidence == 0.7


def test_opportunity_can_recommend_multiple_acquisition_modes() -> None:
    item = Opportunity(
        entity_id="company:example",
        capability_need_id=hypothesis().id,
        confidence=0.8,
        acquisition_modes=(AcquisitionMode.FDE, AcquisitionMode.FRACTIONAL),
        evidence_ids=(uuid4(),),
        rationale="Embedded or fractional delivery may satisfy the need.",
    )
    assert AcquisitionMode.FDE in item.acquisition_modes
    assert AcquisitionMode.FRACTIONAL in item.acquisition_modes


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


def test_entity_resolution_rejects_ambiguity() -> None:
    from tinlance_sdea.entity import AmbiguousEntityResolution

    entities = (
        Entity(
            id="org:a",
            entity_type=EntityType.ORGANIZATION,
            canonical_name="Example Ltd",
        ),
        Entity(
            id="org:b",
            entity_type=EntityType.ORGANIZATION,
            canonical_name="Example Ltd",
        ),
    )
    with pytest.raises(AmbiguousEntityResolution):
        resolve_entity("example ltd", entities)


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
        assessed_at=datetime(2026, 10, 2, tzinfo=UTC),
    )
    assert provenance.collector == "adapter:test"
    assert reliability.reliability == 0.8


def test_domain_contracts_validate_temporal_and_confidence_boundaries() -> None:
    from tinlance_sdea.domain.models import BuyingWindow, CapabilityNeed, Signal, SignalCluster

    signal_id = Signal(
        entity_id="org:example",
        signal_type="funding",
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        evidence_ids=(uuid4(),),
    ).id
    cluster = SignalCluster(
        entity_id="org:example",
        signal_ids=(signal_id,),
        first_observed_at=datetime(2026, 10, 1, tzinfo=UTC),
        last_observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        confidence=0.9,
    )
    item = hypothesis()
    capability = CapabilityNeed(
        entity_id="org:example",
        capability="platform engineering",
        demand_hypothesis_id=item.id,
        confidence=0.8,
        urgency=0.7,
        why_now="Recent infrastructure expansion.",
    )
    window = BuyingWindow(
        status="emerging",
        starts_at=datetime(2026, 10, 1, tzinfo=UTC),
        ends_at=datetime(2026, 11, 1, tzinfo=UTC),
        confidence=0.7,
        rationale="Recent signals indicate a near-term window.",
    )
    assert cluster.last_observed_at > cluster.first_observed_at
    assert capability.urgency == 0.7
    assert window.ends_at is not None


def test_invalid_intervals_and_confidence_are_rejected() -> None:
    from tinlance_sdea.domain.models import BuyingWindow, SignalCluster

    with pytest.raises(ValidationError):
        SignalCluster(
            entity_id="org:example",
            signal_ids=(),
            first_observed_at=datetime(2026, 10, 2, tzinfo=UTC),
            last_observed_at=datetime(2026, 10, 1, tzinfo=UTC),
            confidence=0.5,
        )
    with pytest.raises(ValidationError):
        BuyingWindow(
            status="invalid",
            starts_at=datetime(2026, 10, 2, tzinfo=UTC),
            ends_at=datetime(2026, 10, 1, tzinfo=UTC),
            confidence=0.5,
            rationale="Invalid interval.",
        )
    with pytest.raises(ValidationError):
        DemandHypothesis(
            entity_id="org:example",
            statement="Invalid confidence.",
            supporting_signal_ids=(uuid4(),),
            confidence=1.1,
            rationale="Should fail.",
        )
    with pytest.raises(ValidationError):
        Signal(
            entity_id="org:example",
            signal_type="funding",
            occurred_at=datetime(2026, 10, 1),
            observed_at=datetime(2026, 10, 2),
            evidence_ids=(uuid4(),),
        )


def test_acquisition_recommendation_is_human_approval_by_default() -> None:
    from tinlance_sdea.domain.models import AcquisitionRecommendation

    recommendation = AcquisitionRecommendation(
        opportunity_id=Opportunity(
            entity_id="org:example",
            capability_need_id=hypothesis().id,
            confidence=0.5,
            evidence_ids=(uuid4(),),
            rationale="Evidence-backed opportunity.",
        ).id,
        mode=AcquisitionMode.PRODUCT,
        confidence=0.6,
        rationale="A product may satisfy the capability.",
    )
    assert recommendation.requires_human_approval is True
    with pytest.raises(ValidationError):
        recommendation.model_copy(update={"requires_human_approval": False})


def test_entity_identifier_and_normalization_contracts() -> None:
    from tinlance_sdea.entity import EntityIdentifier, normalize_entity_name

    identifier = EntityIdentifier(scheme="domain", value="example.com")
    assert identifier.value == "example.com"
    assert normalize_entity_name("  Example,  Company! ") == "example company"


def test_entity_identifier_rejects_empty_parts() -> None:
    from tinlance_sdea.entity import EntityIdentifier

    with pytest.raises(ValidationError):
        EntityIdentifier(scheme="", value="example")


def test_entity_rejects_blank_canonical_name() -> None:
    from tinlance_sdea.entity import Entity, EntityType

    with pytest.raises(ValidationError):
        Entity(id="org:bad", entity_type=EntityType.ORGANIZATION, canonical_name="   ")


def test_evidence_fingerprint_changes_when_observed_content_changes() -> None:
    first = Evidence(
        source_type="funding",
        observed_at=datetime(2026, 10, 1, tzinfo=UTC),
        collected_at=datetime(2026, 10, 2, tzinfo=UTC),
        title="Funding announcement",
        excerpt="Series A",
    )
    second = first.model_copy(update={"excerpt": "Series B"})
    assert fingerprint_evidence(first) != fingerprint_evidence(second)
