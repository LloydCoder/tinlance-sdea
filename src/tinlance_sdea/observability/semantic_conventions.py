"""Versioned SDEA observability semantic conventions."""

from ..contracts.versions import CONTRACT_VERSION, schema_url

SCHEMA_VERSION = CONTRACT_VERSION
SCHEMA_URL = schema_url(SCHEMA_VERSION)
ENTITY_ID = "sdea.entity.id"
SIGNAL_TYPE = "sdea.signal.type"
EVIDENCE_ID = "sdea.evidence.id"
OPPORTUNITY_ID = "sdea.opportunity.id"
