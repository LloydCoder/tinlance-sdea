"""ReconOS integration contract."""

from .._shared import IntegrationContract


class ReconOSContract(IntegrationContract):
    consumer = "reconos"
    purpose = "account/entity intelligence input"
