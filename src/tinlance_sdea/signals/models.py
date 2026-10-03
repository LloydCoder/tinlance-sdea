"""Canonical normalized signal contracts."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class SignalRecord(SDEAModel):
    """A source-normalized organizational signal with evidence lineage."""

    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    signal_type: str
    source_event_id: str
    occurred_at: datetime
    observed_at: datetime
    evidence_ids: tuple[UUID, ...]
    attributes: dict[str, str] = Field(default_factory=dict)
    fingerprint: str | None = None

    @model_validator(mode="after")
    def validate_chronology(self) -> SignalRecord:
        if self.observed_at < self.occurred_at:
            raise ValueError("observed_at cannot be earlier than occurred_at")
        if not self.evidence_ids:
            raise ValueError("a normalized signal must reference at least one evidence item")
        return self
