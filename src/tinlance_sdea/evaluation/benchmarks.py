"""Benchmark case registry."""

from .regression import RegressionCase


def benchmark_cases() -> tuple[RegressionCase, ...]:
    return (
        RegressionCase(
            case_id="SDEA-001",
            expected="evidence-backed-demand",
            observed="evidence-backed-demand",
        ),
    )
