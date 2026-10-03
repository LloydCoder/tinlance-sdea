"""Regression evaluation contracts."""

from pydantic import Field
from ..domain.models import SDEAModel


class RegressionCase(SDEAModel):
    case_id: str
    expected: str
    observed: str


class RegressionResult(SDEAModel):
    case_id: str
    passed: bool
    score: float = Field(ge=0.0, le=1.0)
