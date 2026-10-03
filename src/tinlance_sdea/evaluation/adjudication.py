"""Human adjudication contracts."""

from pydantic import Field
from ..domain.models import SDEAModel


class Adjudication(SDEAModel):
    case_id: str
    decision: str
    reviewer: str
    confidence: float = Field(ge=0.0, le=1.0)
