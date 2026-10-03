"""Deterministic redaction helpers."""

import re

_EMAIL = re.compile(r"[^\s@]+@[^\s@]+\.[^\s@]+")


def redact_email(value: str) -> str:
    return _EMAIL.sub("[REDACTED_EMAIL]", value)
