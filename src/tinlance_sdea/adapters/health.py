"""Adapter health contracts."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class AdapterHealth(StrEnum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    DISABLED = "disabled"


class AdapterHealthReport(SDEAModel):
    """Operational health snapshot for a signal adapter."""

    adapter_name: str
    status: AdapterHealth
    checked_at: datetime
    message: str = ""
    latency_ms: float = Field(default=0.0, ge=0.0)

    @model_validator(mode="after")
    def validate_report(self) -> AdapterHealthReport:
        if not self.adapter_name.strip():
            raise ValueError("adapter_name must be non-empty")
        if self.checked_at.tzinfo is None or self.checked_at.utcoffset() is None:
            raise ValueError("checked_at must be timezone-aware")
        return self
