"""Outcome intelligence contracts."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class OutcomeEvent(SDEAModel):
    id: UUID
    opportunity_id: UUID
    event_type: str
    occurred_at: datetime
    value: float | None = None
    metadata: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_event(self) -> OutcomeEvent:
        if not self.event_type.strip():
            raise ValueError("event_type must be non-empty")
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        return self


class OutcomeAttribution(SDEAModel):
    opportunity_id: UUID
    outcome_event_id: UUID
    attributed: bool
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

    @model_validator(mode="after")
    def validate_attribution(self) -> OutcomeAttribution:
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self
