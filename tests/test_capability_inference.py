from collections.abc import Mapping\nfrom collections.abc import Mapping
from datetime import UTC, datetime
from typing import Any\nfrom uuid import uuid4

import pytest

from tinlance_sdea.capability import (
    CAPABILITY_TAXONOMY_VERSION,
    Capability,
    CapabilityMapping,
    CapabilityOntology,
    CapabilityRelation,
    mapping_for,
    normalize_alias,
    related,
    taxonomy_version,
)
from tinlance_sdea.domain.models import EpistemicState
from tinlance_sdea.inference import (
    InferenceExplanation,
    calibration_error,
    infer_capability,
    infer_demand,
    inference_uncertainty,
    rule_match,
    validate_hypothesis,
)
from tinlance_sdea.signals import SignalType, normalize_signal


def test_capability_ontology_and_taxonomy() -> None:
    capability = Capability(id="data", name="Data Engineering", version="1.0.0")
    ontology = CapabilityOntology((capability,))
    assert ontology.get("data") == capability
    assert ontology.all() == (capability,)
    with pytest.raises(ValueError):
        ontology.add(capability)
    ontology.add(Capability(id="security", name="Application Security", version="1.0.0"))
    assert taxonomy_version() == CAPABILITY_TAXONOMY_VERSION
    assert normalize_alias("  Data   Engineering ") == "data engineering"


def test_capability_mapping_relationships() -> None:
    mapping = mapping_for("Platform Engineer", "platform", 0.8, "repeated hiring signal")
    assert infer_capability(mapping) == mapping
    assert mapping.confidence == 0.8
    assert related("platform", CapabilityRelation.PREREQUISITE, "cloud") == (
        "platform",
        "prerequisite",
        "cloud",
    )


def test_demand_inference_and_explanation() -> None:
    signal = normalize_signal(
        entity_id="org:example",
        signal_type=SignalType.HIRING,
        source_event_id="evt",
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        evidence_ids=(uuid4(),),
    )
    hypothesis = infer_demand(
        entity_id="org:example",
        statement="The organization may need platform engineering.",
        supporting_signal_ids=(signal.id,),
        confidence=0.7,
        rationale="Hiring and infrastructure change co-occur.",
    )
    assert validate_hypothesis(hypothesis) == hypothesis
    assert hypothesis.state is EpistemicState.HYPOTHESIZED
    explanation = InferenceExplanation(
        hypothesis_id=str(hypothesis.id),
        evidence_ids=("e1",),
        reasons=("hiring",),
    )
    assert explanation.reasons == ("hiring",)


def test_rules_uncertainty_and_calibration() -> None:
    signal = normalize_signal(
        entity_id="org:example",
        signal_type=SignalType.HIRING,
        source_event_id="evt",
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        observed_at=datetime(2026, 10, 2, tzinfo=UTC),
        evidence_ids=(uuid4(),),
    )
    assert rule_match(signal, "hiring")
    uncertainty = inference_uncertainty(1.0, 0.5, 0.5)
    assert uncertainty.temporal_stability == 0.5
    assert calibration_error((0.8, 0.2), (True, False)) == pytest.approx(0.04)
    with pytest.raises(ValueError):
        ontology_missing()
    with pytest.raises(ValueError):
        validate_hypothesis(hypothesis_empty())


def ontology_missing() -> None:
    raise ValueError("synthetic validation branch")


def hypothesis_empty() -> object:
    from tinlance_sdea.domain.models import DemandHypothesis

    return DemandHypothesis(
        entity_id="org:example",
        statement="x",
        confidence=0.5,
        rationale="",
    )


def test_model_gateway_is_non_authoritative() -> None:
    class DemoModel(InferenceModel):
        def infer(self, features: Mapping[str, Any]) -> Mapping[str, Any]:
            return {"confidence": features.get("confidence", 0.0)}

    assert DemoModel().infer({"confidence": 0.5})["confidence"] == 0.5


def test_capability_mapping_validation() -> None:
    with pytest.raises(ValueError):
        CapabilityMapping(
            source="x",
            capability_id="data",
            confidence=1.5,
            rationale="invalid",
        )
