"""FadeReach integration contract."""

from .._shared import IntegrationContract


class FadeReachContract(IntegrationContract):
    consumer: str = "fadereach"
    purpose: str = "human-approved opportunity handoff"
