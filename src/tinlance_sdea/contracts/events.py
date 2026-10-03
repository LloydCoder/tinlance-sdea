"""Integration event contracts."""

from datetime import datetime

from pydantic import Field, model_validator

from ..domain.models import SDEAModel
from .versions import CONTRACT_VERSION, validate_version


class SDEAEvent(SDEAModel):
    event_name: str
    schema_version: str = CONTRACT_VERSION
    occurred_at: datetime
    entity_id: str
    payload: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_event(self) -> SDEAEvent:
        if not self.event_name.strip():
            raise ValueError("event_name must be non-empty")
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        validate_version(self.schema_version)
        return self
