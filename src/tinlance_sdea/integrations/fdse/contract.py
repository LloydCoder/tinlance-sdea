"""FDSE integration contract."""

from .._shared import IntegrationContract


class FDSEContract(IntegrationContract):
    consumer: str = "fdse"
    purpose: str = "engineering-delivery handoff"
