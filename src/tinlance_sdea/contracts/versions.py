"""Versioned SDEA contract metadata."""

import re

CONTRACT_VERSION = "1.0.0"
SCHEMA_FAMILY = "https://tinlance.com/sdea/schema"
_SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def validate_version(version: str) -> str:
    """Validate the strict SemVer subset used by SDEA wire contracts."""

    if not _SEMVER.fullmatch(version):
        raise ValueError(f"invalid contract version: {version!r}")
    return version


def schema_url(version: str = CONTRACT_VERSION) -> str:
    """Return the stable schema URL for a contract version."""

    validate_version(version)
    return f"{SCHEMA_FAMILY}/{version}"
