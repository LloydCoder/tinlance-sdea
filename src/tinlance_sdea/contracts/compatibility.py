"""Contract compatibility rules."""


def compatible(producer_version: str, consumer_version: str) -> bool:
    """Allow same-major semantic versions."""

    return producer_version.split(".", 1)[0] == consumer_version.split(".", 1)[0]
