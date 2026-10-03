"""Evidence provenance contracts."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field, HttpUrl

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
