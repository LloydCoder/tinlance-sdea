"""FDSE integration contract."""

from .._shared import IntegrationContract


class FDSEContract(IntegrationContract):
    consumer = "fdse"
    purpose = "engineering-delivery handoff"
