"""Shared integration contract."""

from pydantic import Field

from ..domain.models import SDEAModel


class IntegrationContract(SDEAModel):
    consumer: str
    purpose: str
    contract_version: str = "1.0.0"
    allowed_actions: tuple[str, ...] = Field(default_factory=tuple)
