"""ReconOS integration contract."""

from .._shared import IntegrationContract


class ReconOSContract(IntegrationContract):
    consumer: str = "reconos"
    purpose: str = "account/entity intelligence input"
