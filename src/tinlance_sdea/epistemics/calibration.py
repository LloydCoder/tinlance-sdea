"""Calibration metrics."""

from collections.abc import Sequence


def brier_score(predictions: Sequence[float], outcomes: Sequence[bool]) -> float:
    """Compute mean squared probability error."""

    if len(predictions) != len(outcomes):
        raise ValueError("predictions and outcomes must have equal length")
    if not predictions:
        return 0.0
    if any(not 0.0 <= value <= 1.0 for value in predictions):
        raise ValueError("predictions must be between 0 and 1")
    return sum(
        (prediction - float(outcome)) ** 2
        for prediction, outcome in zip(predictions, outcomes)
    ) / len(predictions)
