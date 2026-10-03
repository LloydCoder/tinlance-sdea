"""Time interval contracts."""

from datetime import datetime

from pydantic import model_validator

from ..domain.models import SDEAModel


class TimeInterval(SDEAModel):
    start: datetime
    end: datetime

    @model_validator(mode="after")
    def validate_order(self) -> "TimeInterval":
        if self.end < self.start:
            raise ValueError("interval end cannot precede start")
        return self
