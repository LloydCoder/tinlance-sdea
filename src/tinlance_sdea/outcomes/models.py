"""Outcome intelligence contracts."""

from datetime import datetime
from uuid import UUID
from pydantic import Field
from ..domain.models import SDEAModel


class OutcomeEvent(SDEAModel):
    id: UUID
    opportunity_id: UUID
    event_type: str
    occurred_at: datetime
    value: float | None = None
    metadata: dict[str, str] = {}


class OutcomeAttribution(SDEAModel):
    opportunity_id: UUID
    outcome_event_id: UUID
    attributed: bool
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
