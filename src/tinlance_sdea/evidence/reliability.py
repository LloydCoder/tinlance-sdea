"""Source reliability metadata."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class SourceReliability(SDEAModel):
    source_name: str
    reliability: float = Field(ge=0.0, le=1.0)
    rationale: str
    assessed_at: datetime

    @model_validator(mode="after")
    def validate_reliability(self) -> SourceReliability:
        if not self.source_name.strip():
            raise ValueError("source_name must be non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        if self.assessed_at.tzinfo is None or self.assessed_at.utcoffset() is None:
            raise ValueError("assessed_at must be timezone-aware")
        return self
