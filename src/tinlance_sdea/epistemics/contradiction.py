"""Epistemic contradiction contracts."""

from pydantic import Field

from ..domain.models import SDEAModel


class Contradiction(SDEAModel):
    """Explicit contradiction between evidence-backed claims."""

    left_id: str
    right_id: str
    reason: str
    severity: float = Field(ge=0.0, le=1.0)
