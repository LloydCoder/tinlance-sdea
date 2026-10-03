"""Opportunity handoff construction."""

from uuid import UUID

from .models import OpportunityHandoff


def make_handoff(
    opportunity_id: UUID,
    entity_id: str,
    capability_id: str,
    confidence: float,
    evidence_ids: tuple[UUID, ...],
    rationale: str,
) -> OpportunityHandoff:
    return OpportunityHandoff(
        opportunity_id=opportunity_id,
        entity_id=entity_id,
        capability_id=capability_id,
        confidence=confidence,
        evidence_ids=evidence_ids,
        rationale=rationale,
    )
