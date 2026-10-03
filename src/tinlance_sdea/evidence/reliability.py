"""Source reliability metadata."""

from __future__ import annotations

from pydantic import Field

from ..domain.models import SDEAModel


class SourceReliability(SDEAModel):
    source_name: str
    reliability: float = Field(ge=0.0, le=1.0)
    rationale: str
    assessed_at: str
