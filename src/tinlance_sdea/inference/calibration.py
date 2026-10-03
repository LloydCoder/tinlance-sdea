"""Inference calibration facade."""

from collections.abc import Sequence

from ..epistemics.calibration import brier_score


def calibration_error(predictions: Sequence[float], outcomes: Sequence[bool]) -> float:
    return brier_score(predictions, outcomes)
