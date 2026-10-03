"""Temporal relation classification."""

from enum import StrEnum

from .intervals import TimeInterval


class TemporalRelation(StrEnum):
    BEFORE = "before"
    AFTER = "after"
    OVERLAPS = "overlaps"
    CONTAINS = "contains"
    EQUAL = "equal"


def relate(left: TimeInterval, right: TimeInterval) -> TemporalRelation:
    """Classify the deterministic relation between two intervals."""

    if left.end < right.start:
        return TemporalRelation.BEFORE
    if left.start > right.end:
        return TemporalRelation.AFTER
    if left.start == right.start and left.end == right.end:
        return TemporalRelation.EQUAL
    if left.start <= right.start and left.end >= right.end:
        return TemporalRelation.CONTAINS
    return TemporalRelation.OVERLAPS
