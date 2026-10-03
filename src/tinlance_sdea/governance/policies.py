"""Data-governance policy evaluation."""

from .classification import DataClass, can_share


def permitted(source: DataClass, target_clearance: DataClass) -> bool:
    """Compatibility facade for the classification sharing rule."""

    return can_share(source, target_clearance)
