"""Opportunity explanation contracts."""

from pydantic import Field

from ..domain.models import SDEAModel


class OpportunityExplanation(SDEAModel):
    opportunity_id: str
    evidence_ids: tuple[str, ...] = ()
    reasons: tuple[str, ...] = Field(default_factory=tuple)
