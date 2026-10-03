"""Contract compatibility rules."""

from .versions import validate_version


def compatible(producer_version: str, consumer_version: str) -> bool:
    """Allow consumers to accept the same-major semantic-version family."""

    producer = validate_version(producer_version)
    consumer = validate_version(consumer_version)
    return producer.split(".", 1)[0] == consumer.split(".", 1)[0]
