"""Deterministic entity-name normalization helpers."""

import unicodedata


def normalize_entity_name(value: str) -> str:
    """Normalize an entity name for deterministic comparison, not display."""

    normalized = unicodedata.normalize("NFKC", value).strip().casefold()
    normalized = "".join(char if char.isalnum() else " " for char in normalized)
    return " ".join(normalized.split())
