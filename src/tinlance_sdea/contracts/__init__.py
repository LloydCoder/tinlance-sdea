"""Versioned SDEA contract surface."""

from .compatibility import compatible
from .events import SDEAEvent
from .json_schema import json_schema
from .serialization import serialize
from .versions import CONTRACT_VERSION, SCHEMA_FAMILY, schema_url, validate_version

__all__ = [
    "CONTRACT_VERSION",
    "SCHEMA_FAMILY",
    "SDEAEvent",
    "compatible",
    "json_schema",
    "schema_url",
    "serialize",
    "validate_version",
]
