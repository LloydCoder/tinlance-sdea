"""Calibration evaluation facade."""

from collections.abc import Sequence
from ..epistemics.calibration import brier_score


def brier(predictions: Sequence[float], outcomes: Sequence[bool]) -> float:
    return brier_score(predictions, outcomes)
