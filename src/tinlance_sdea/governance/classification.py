"""Data classification contracts."""

from enum import StrEnum


class DataClass(StrEnum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


_RANK = {
    DataClass.PUBLIC: 0,
    DataClass.INTERNAL: 1,
    DataClass.CONFIDENTIAL: 2,
    DataClass.RESTRICTED: 3,
}


def can_share(source: DataClass, target_clearance: DataClass) -> bool:
    """Return whether a target clearance is sufficient for source sensitivity."""

    return _RANK[target_clearance] >= _RANK[source]
