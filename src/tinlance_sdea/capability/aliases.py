"""Capability alias normalization."""


def normalize_alias(value: str) -> str:
    """Normalize a capability alias for lookup."""

    return " ".join(value.casefold().split())
