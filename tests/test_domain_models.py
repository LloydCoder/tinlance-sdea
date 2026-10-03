from tinlance_sdea.domain.models import AcquisitionMode, DemandHypothesis, Opportunity

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