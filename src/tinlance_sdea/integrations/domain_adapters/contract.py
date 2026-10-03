"""Domain adapter integration contract."""

from .._shared import IntegrationContract


class DomainAdapterContract(IntegrationContract):
    consumer: str = "domain_adapter"
    purpose: str = "source-specific signal translation"
