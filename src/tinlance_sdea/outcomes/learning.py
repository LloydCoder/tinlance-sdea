"""Learning signals from outcomes."""

from collections.abc import Sequence


def improvement_delta(before: float, after: float) -> float:
    return after - before


def outcome_rate(values: Sequence[bool]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)
