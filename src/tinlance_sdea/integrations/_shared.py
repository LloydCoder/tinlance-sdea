"""Shared integration contract."""

from __future__ import annotations

from pydantic import Field, model_validator

from ..contracts.versions import CONTRACT_VERSION, validate_version
from ..domain.models import SDEAModel


class IntegrationContract(SDEAModel):
    consumer: str
    purpose: str
    contract_version: str = CONTRACT_VERSION
    allowed_actions: tuple[str, ...] = Field(default_factory=tuple)

    @model_validator(mode="after")
    def validate_contract(self) -> IntegrationContract:
        if not self.consumer.strip():
            raise ValueError("consumer must be non-empty")
        if not self.purpose.strip():
            raise ValueError("purpose must be non-empty")
        validate_version(self.contract_version)
        if len(set(self.allowed_actions)) != len(self.allowed_actions):
            raise ValueError("allowed_actions must be unique")
        return self
