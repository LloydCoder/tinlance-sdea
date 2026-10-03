"""Integration event contracts."""

from datetime import datetime

from pydantic import Field

from ..domain.models import SDEAModel


class SDEAEvent(SDEAModel):
    event_name: str
    schema_version: str
    occurred_at: datetime
    entity_id: str
    payload: dict[str, str] = Field(default_factory=dict)
