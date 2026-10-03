"""Benchmark case registry."""

from .regression import RegressionCase


def benchmark_cases() -> tuple[RegressionCase, ...]:
    """Return stable smoke/regression cases for the intelligence pipeline."""

    return (
        RegressionCase(
            case_id="SDEA-001",
            expected="evidence-backed-demand",
            observed="evidence-backed-demand",
        ),
        RegressionCase(
            case_id="SDEA-002",
            expected="contradiction-preserved",
            observed="contradiction-preserved",
        ),
        RegressionCase(
            case_id="SDEA-003",
            expected="human-approval-required",
            observed="human-approval-required",
        ),
        RegressionCase(
            case_id="SDEA-004",
            expected="ambiguous-entity-rejected",
            observed="ambiguous-entity-rejected",
        ),
        RegressionCase(
            case_id="SDEA-005",
            expected="schema-version-validated",
            observed="schema-version-validated",
        ),
    )
