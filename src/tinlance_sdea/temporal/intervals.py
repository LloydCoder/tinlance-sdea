"""Time interval contracts."""

from __future__ import annotations

from datetime import datetime

from pydantic import model_validator

from ..domain.models import SDEAModel


class TimeInterval(SDEAModel):
    start: datetime
    end: datetime

    @model_validator(mode="after")
    def validate_order(self) -> TimeInterval:
        for name, value in (("start", self.start), ("end", self.end)):
            if value.tzinfo is None or value.utcoffset() is None:
                raise ValueError(f"{name} must be timezone-aware")
        if self.end < self.start:
            raise ValueError("interval end cannot precede start")
        return self
