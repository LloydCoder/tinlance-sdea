"""Adapter health contracts."""

from enum import StrEnum

from pydantic import Field

from ..domain.models import SDEAModel


class AdapterHealth(StrEnum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    DISABLED = "disabled"


class AdapterHealthReport(SDEAModel):
    """Operational health snapshot for a signal adapter."""

    adapter_name: str
    status: AdapterHealth
    checked_at: str
    message: str = ""
    latency_ms: float = Field(default=0.0, ge=0.0)
