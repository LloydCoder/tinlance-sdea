"""Versioned canonical signal taxonomy."""

from enum import StrEnum


class SignalType(StrEnum):
    """Source-agnostic signal types representing organizational change."""

    HIRING = "hiring"
    FUNDING = "funding"
    PRODUCT_CHANGE = "product_change"
    TECHNOLOGY_CHANGE = "technology_change"
    AI_ADOPTION = "ai_adoption"
    SECURITY_EVENT = "security_event"
    INFRASTRUCTURE_CHANGE = "infrastructure_change"
    LEADERSHIP_CHANGE = "leadership_change"
    EXPANSION = "expansion"
    REGULATORY_CHANGE = "regulatory_change"
    PARTNERSHIP = "partnership"
    ACQUISITION = "acquisition"
    PROCUREMENT = "procurement"
    OPEN_SOURCE = "open_source"
    PRICING_CHANGE = "pricing_change"
    CUSTOMER_EXPANSION = "customer_expansion"
    PRODUCT_SUNSET = "product_sunset"
    OTHER = "other"


SIGNAL_TAXONOMY_VERSION = "1.0.0"
