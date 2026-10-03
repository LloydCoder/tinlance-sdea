"""Deterministic entity-name normalization helpers."""

import re
import unicodedata


_WHITESPACE = re.compile(r"\s+")
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def normalize_entity_name(value: str) -> str:
    """Normalize an entity name for deterministic comparison, not display."""

    normalized = unicodedata.normalize("NFKC", value).strip().casefold()
    normalized = _NON_ALNUM.sub(" ", normalized)
    return _WHITESPACE.sub(" ", normalized).strip()
