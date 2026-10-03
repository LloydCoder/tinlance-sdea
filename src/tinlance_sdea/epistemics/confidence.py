"""Confidence composition."""

from collections.abc import Sequence


def combine_confidence(values: Sequence[float]) -> float:
    """Combine independent confidence estimates conservatively."""

    if not values:
        return 0.0
    if any(not 0.0 <= value <= 1.0 for value in values):
        raise ValueError("confidence values must be between 0 and 1")
    return sum(values) / len(values)
