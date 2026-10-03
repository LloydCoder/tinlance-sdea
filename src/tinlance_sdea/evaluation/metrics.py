"""Evaluation metrics."""

from collections.abc import Sequence


def precision(predicted: Sequence[bool], actual: Sequence[bool]) -> float:
    if len(predicted) != len(actual):
        raise ValueError("predicted and actual must have equal length")
    positives = sum(predicted)
    if positives == 0:
        return 0.0
    true_positive = sum(p and a for p, a in zip(predicted, actual, strict=True))
    return true_positive / positives


def recall(predicted: Sequence[bool], actual: Sequence[bool]) -> float:
    if len(predicted) != len(actual):
        raise ValueError("predicted and actual must have equal length")
    actual_positive = sum(actual)
    if actual_positive == 0:
        return 0.0
    true_positive = sum(p and a for p, a in zip(predicted, actual, strict=True))
    return true_positive / actual_positive
