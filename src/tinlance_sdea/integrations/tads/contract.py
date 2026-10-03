"""TADS integration contract."""

from .._shared import IntegrationContract


class TADSContract(IntegrationContract):
    consumer: str = "tads"
    purpose: str = "demand-intelligence workflow consumption"
