"""Epistemic assessment state contracts."""

from pydantic import Field

from ..domain.models import EpistemicState, SDEAModel


class EpistemicAssessment(SDEAModel):
    """State, confidence and rationale independent of lifecycle."""

    state: EpistemicState
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


def assess(state: EpistemicState, confidence: float, rationale: str) -> EpistemicAssessment:
    """Create a validated epistemic assessment."""

    return EpistemicAssessment(state=state, confidence=confidence, rationale=rationale)
