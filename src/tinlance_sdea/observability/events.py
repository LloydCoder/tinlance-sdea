"""SDEA observability events."""

from __future__ import annotations

import re
from datetime import datetime

from pydantic import Field, model_validator

from ..domain.models import SDEAModel

_EVENT_NAME = re.compile(r"^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_]*)+$")


class ObservabilityEvent(SDEAModel):
    name: str
    occurred_at: datetime
    attributes: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_event(self) -> ObservabilityEvent:
        if not _EVENT_NAME.fullmatch(self.name):
            raise ValueError("event name must be a stable dot-delimited identifier")
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        return self
