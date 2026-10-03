"""Evaluation and regression contracts."""

from .adjudication import Adjudication
from .benchmarks import benchmark_cases
from .calibration import brier
from .metrics import precision, recall
from .regression import RegressionCase, RegressionResult, evaluate_cases

__all__ = [
    "Adjudication",
    "RegressionCase",
    "RegressionResult",
    "benchmark_cases",
    "brier",
    "evaluate_cases",
    "precision",
    "recall",
]
