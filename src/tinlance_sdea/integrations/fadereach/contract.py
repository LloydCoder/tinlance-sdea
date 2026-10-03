"""FadeReach integration contract."""

from .._shared import IntegrationContract


class FadeReachContract(IntegrationContract):
    consumer = "fadereach"
    purpose = "human-approved opportunity handoff"
