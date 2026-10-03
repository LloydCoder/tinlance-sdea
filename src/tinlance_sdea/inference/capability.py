"""Capability inference primitives."""

from ..capability.models import CapabilityMapping


def infer_capability(mapping: CapabilityMapping) -> CapabilityMapping:
    """Return a validated mapping without changing authority."""

    return mapping
