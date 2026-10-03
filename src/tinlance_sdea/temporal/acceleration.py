"""Temporal acceleration metrics."""


def acceleration_ratio(*, recent_count: int, prior_count: int) -> float:
    """Compare recent activity with the preceding comparable period."""

    if prior_count < 0 or recent_count < 0:
        raise ValueError("counts cannot be negative")
    if prior_count == 0:
        return 1.0 if recent_count > 0 else 0.0
    return recent_count / prior_count
