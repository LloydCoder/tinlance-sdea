"""Regression evaluation contracts."""

from __future__ import annotations

from collections.abc import Iterable

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class RegressionCase(SDEAModel):
    case_id: str
    expected: str
    observed: str

    @model_validator(mode="after")
    def validate_case(self) -> RegressionCase:
        if not self.case_id.strip():
            raise ValueError("case_id must be non-empty")
        if not self.expected.strip() or not self.observed.strip():
            raise ValueError("expected and observed must be non-empty")
        return self


class RegressionResult(SDEAModel):
    case_id: str
    passed: bool
    score: float = Field(ge=0.0, le=1.0)


def evaluate_cases(cases: Iterable[RegressionCase]) -> tuple[RegressionResult, ...]:
    """Evaluate deterministic regression cases without model authority."""

    return tuple(
        RegressionResult(
            case_id=case.case_id,
            passed=case.expected == case.observed,
            score=1.0 if case.expected == case.observed else 0.0,
        )
        for case in cases
    )
