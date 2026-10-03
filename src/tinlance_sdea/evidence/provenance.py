"""Evidence provenance contracts."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field, HttpUrl, model_validator

from ..domain.models import SDEAModel


class Provenance(SDEAModel):
    """Trace where an evidence item came from and when it was collected."""

    source_name: str
    source_type: str
    source_url: HttpUrl | None = None
    artifact_id: str | None = None
    collected_at: datetime
    collector: str
    parent_provenance_id: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_provenance(self) -> Provenance:
        if not self.source_name.strip():
            raise ValueError("source_name must be non-empty")
        if not self.source_type.strip():
            raise ValueError("source_type must be non-empty")
        if not self.collector.strip():
            raise ValueError("collector must be non-empty")
        if self.collected_at.tzinfo is None or self.collected_at.utcoffset() is None:
            raise ValueError("collected_at must be timezone-aware")
        return self
