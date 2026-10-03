"""Opportunity qualification rules."""

from ..domain.models import EpistemicState, LifecycleState, Opportunity


def qualify(opportunity: Opportunity) -> bool:
    """Return whether an opportunity meets the minimum handoff contract."""

    return (
        opportunity.lifecycle_state is LifecycleState.ACTIVE
        and opportunity.state in {EpistemicState.QUALIFIED, EpistemicState.CONFIRMED}
        and bool(opportunity.evidence_ids)
        and opportunity.confidence > 0.0
        and bool(opportunity.rationale.strip())
    )
