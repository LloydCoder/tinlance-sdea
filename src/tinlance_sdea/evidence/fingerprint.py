"""Deterministic evidence fingerprinting."""

from __future__ import annotations

import hashlib

from ..domain.models import Evidence


def fingerprint_evidence(evidence: Evidence) -> str:
    """Return a stable SHA-256 fingerprint for the observed evidence semantics.

    Collection time is excluded so re-collection of the same observed artifact
    can reconcile to the same evidence identity.
    """

    parts = (
        evidence.source_type.value,
        str(evidence.source_url or ""),
        evidence.observed_at.isoformat(),
        evidence.title.strip().casefold(),
        (evidence.excerpt or "").strip(),
        evidence.content_hash or "",
    )
    payload = "\x1f".join(parts).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
