"""SDEA observability events."""

from datetime import datetime

from pydantic import Field

from ..domain.models import SDEAModel


class ObservabilityEvent(SDEAModel):
    name: str
    occurred_at: datetime
    attributes: dict[str, str] = Field(default_factory=dict)
