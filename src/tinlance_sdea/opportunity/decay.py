"""Opportunity decay facade."""

from ..temporal.decay import decay_score


def opportunity_decay(age_days: float, half_life_days: float) -> float:
    return decay_score(age_days=age_days, half_life_days=half_life_days)
