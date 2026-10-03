"""TADS integration contract."""

from .._shared import IntegrationContract


class TADSContract(IntegrationContract):
    consumer = "tads"
    purpose = "demand-intelligence workflow consumption"
