"""Recency scoring."""

from datetime import UTC, datetime
from math import exp


def recency_score(*, observed_at: datetime, now: datetime, half_life_days: float) -> float:
    """Return exponential recency in [0, 1]."""

    if half_life_days <= 0:
        raise ValueError("half_life_days must be positive")
    for name, value in (("observed_at", observed_at), ("now", now)):
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError(f"{name} must be timezone-aware")
    age_days = max((now - observed_at).total_seconds() / 86400.0, 0.0)
    return exp(-0.69314718056 * age_days / half_life_days)


def utc_now() -> datetime:
    """Return an offset-aware UTC timestamp."""

    return datetime.now(UTC)
