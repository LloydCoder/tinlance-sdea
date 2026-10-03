"""Opportunity and signal decay helpers."""

from math import exp


def decay_score(*, age_days: float, half_life_days: float) -> float:
    """Return remaining signal weight after elapsed time."""

    if age_days < 0:
        raise ValueError("age_days cannot be negative")
    if half_life_days <= 0:
        raise ValueError("half_life_days must be positive")
    return exp(-0.69314718056 * age_days / half_life_days)
