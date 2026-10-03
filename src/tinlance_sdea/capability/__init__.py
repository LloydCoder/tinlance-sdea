"""Capability intelligence contracts."""

from .aliases import normalize_alias
from .mappings import mapping_for
from .models import Capability, CapabilityMapping
from .ontology import CapabilityOntology
from .relationships import CapabilityRelation, related
from .taxonomy import CAPABILITY_TAXONOMY_VERSION, CORE_CAPABILITIES
from .versioning import taxonomy_version

__all__ = [
    "CAPABILITY_TAXONOMY_VERSION",
    "CORE_CAPABILITIES",
    "Capability",
    "CapabilityMapping",
    "CapabilityOntology",
    "CapabilityRelation",
    "mapping_for",
    "normalize_alias",
    "related",
    "taxonomy_version",
]
