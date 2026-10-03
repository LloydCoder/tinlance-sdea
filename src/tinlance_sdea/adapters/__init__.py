"""Signal source-adapter contracts."""

from .base import SignalAdapter
from .capabilities import AdapterCapability
from .health import AdapterHealth, AdapterHealthReport
from .registry import AdapterRegistry

__all__ = [
    "AdapterAdapter",
    "AdapterCapability",
    "AdapterHealth",
    "AdapterHealthReport",
    "AdapterRegistry",
    "SignalAdapter",
]
