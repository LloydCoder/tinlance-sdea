"""Outcome attribution helpers."""

from uuid import UUID

from .models import OutcomeAttribution


def attribute(
    opportunity_id: UUID,
    outcome_event_id: UUID,
    confidence: float,
    rationale: str,
    attributed: bool = True,
) -> OutcomeAttribution:
    return OutcomeAttribution(
        opportunity_id=opportunity_id,
        outcome_event_id=outcome_event_id,
        attributed=attributed,
        confidence=confidence,
        rationale=rationale,
    )
