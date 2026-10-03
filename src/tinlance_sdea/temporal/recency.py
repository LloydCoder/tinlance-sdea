"""Recency scoring."""

from datetime import UTC, datetime
from math import exp


def recency_score(*, observed_at: datetime, now: datetime, half_life_days: float) -> float:
    """Return exponential recency in [0, 1]."""

    if half_life_days <= 0:
        raise ValueError("half_life_days must be positive")
    age_days = max((now - observed_at).total_seconds() / 86400.0, 0.0)
    return exp(-0.69314718056 * age_days / half_life_days)


def utc_now() -> datetime:
    """Return an offset-aware UTC timestamp."""

    return datetime.now(UTC)
