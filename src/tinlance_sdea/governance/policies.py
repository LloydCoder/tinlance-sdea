"""Data-governance policy evaluation."""

from .classification import DataClass


def permitted(source: DataClass, target: DataClass) -> bool:
    return source is DataClass.RESTRICTED or target is DataClass.PUBLIC or source == target
