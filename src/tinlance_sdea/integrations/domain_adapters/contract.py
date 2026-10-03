"""Domain adapter integration contract."""

from .._shared import IntegrationContract


class DomainAdapterContract(IntegrationContract):
    consumer = "domain_adapter"
    purpose = "source-specific signal translation"
