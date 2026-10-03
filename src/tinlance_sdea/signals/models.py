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
        for name, value in (("occurred_at", self.occurred_at), ("observed_at", self.observed_at)):
            if value.tzinfo is None or value.utcoffset() is None:
                raise ValueError(f"{name} must be timezone-aware")
        if self.observed_at < self.occurred_at:
            raise ValueError("observed_at cannot be earlier than occurred_at")
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.signal_type.strip():
            raise ValueError("signal_type must be non-empty")
        if not self.source_event_id.strip():
            raise ValueError("source_event_id must be non-empty")
        if not self.evidence_ids:
            raise ValueError("a normalized signal must reference at least one evidence item")
        return self
