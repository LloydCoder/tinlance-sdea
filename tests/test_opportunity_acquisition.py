from datetime import UTC, datetime
from uuid import uuid4

import pytest

from tinlance_sdea.acquisition import (
    AcquisitionConstraint,
    AcquisitionExplanation,
    allowed_modes,
    recommend,
)
from tinlance_sdea.domain.models import AcquisitionMode, LifecycleState, Opportunity
from tinlance_sdea.opportunity import (
    OpportunityExplanation,
    OpportunityGraph,
    buying_window,
    graph_from_edges,
    make_handoff,
    opportunity_decay,
    qualify,
    transition,
)


def opportunity() -> Opportunity:
    return Opportunity(
        entity_id="org:example",
        capability_need_id=uuid4(),
        confidence=0.8,
        evidence_ids=(uuid4(),),
        rationale="corroborated demand",
    )


def test_qualification_lifecycle_decay_and_window() -> None:
    item = opportunity()
    assert qualify(item)
    assert opportunity_decay(0, 7) == pytest.approx(1.0)
    assert transition(LifecycleState.ACTIVE, LifecycleState.STALE) is LifecycleState.STALE
    with pytest.raises(ValueError):
        transition(LifecycleState.RESOLVED, LifecycleState.ACTIVE)
    window = buying_window(datetime(2026, 10, 1, tzinfo=UTC), 7)
    assert window.end.day == 8


def test_opportunity_graph_handoff_and_explanation() -> None:
    graph = graph_from_edges(("a", "b"), (("a", "b"),))
    assert isinstance(graph, OpportunityGraph)
    handoff = make_handoff(
        uuid4(),
        "org:example",
        "platform",
        0.8,
        (uuid4(),),
        "evidence-backed capability need",
    )
    assert handoff.capability_id == "platform"
    explanation = OpportunityExplanation(
        opportunity_id=str(handoff.opportunity_id),
        evidence_ids=("e1",),
        reasons=("timing",),
    )
    assert explanation.reasons == ("timing",)


def test_acquisition_constraints_and_recommendation() -> None:
    opportunity_id = uuid4()
    recommendation = recommend(
        opportunity_id, AcquisitionMode.FDE, 0.8, "embedded delivery fits the capability"
    )
    assert recommendation.requires_human_approval
    constraints = (
        AcquisitionConstraint(mode=AcquisitionMode.FDE, allowed=True),
        AcquisitionConstraint(mode=AcquisitionMode.HIRE, allowed=False),
    )
    assert allowed_modes(constraints) == (constraints[0],)
    explanation = AcquisitionExplanation(
        opportunity_id=str(opportunity_id),
        mode=AcquisitionMode.FDE.value,
        reasons=("bounded scope",),
    )
    assert explanation.mode == "fde"


def test_untraceable_opportunity_is_rejected_at_construction() -> None:
    with pytest.raises(ValueError, match="evidence"):
        Opportunity(
            entity_id="org:example",
            capability_need_id=uuid4(),
            confidence=0.8,
            evidence_ids=(),
            rationale="missing evidence",
        )
