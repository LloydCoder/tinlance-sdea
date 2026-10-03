from datetime import UTC, datetime

import pytest

from tinlance_sdea.contracts import (
    CONTRACT_VERSION,
    SDEAEvent,
    compatible,
    json_schema,
    serialize,
)
from tinlance_sdea.integrations._shared import IntegrationContract
from tinlance_sdea.integrations.domain_adapters.contract import DomainAdapterContract
from tinlance_sdea.integrations.fadereach.contract import FadeReachContract
from tinlance_sdea.integrations.fdse.contract import FDSEContract
from tinlance_sdea.integrations.reconos.contract import ReconOSContract
from tinlance_sdea.integrations.tads.contract import TADSContract


def test_contract_versioning_serialization_and_schema() -> None:
    event = SDEAEvent(
        event_name="opportunity.created",
        schema_version=CONTRACT_VERSION,
        occurred_at=datetime(2026, 10, 1, tzinfo=UTC),
        entity_id="org:example",
        payload={"capability": "platform"},
    )
    data = serialize(event)
    schema = json_schema(event)
    assert data["event_name"] == "opportunity.created"
    assert "properties" in schema
    assert compatible("1.2.0", "1.9.0")
    assert not compatible("1.2.0", "2.0.0")
    with pytest.raises(TypeError):
        serialize(object())


def test_integration_contract_boundaries() -> None:
    contracts = (
        TADSContract(),
        ReconOSContract(),
        FadeReachContract(),
        FDSEContract(),
        DomainAdapterContract(),
    )
    assert {item.consumer for item in contracts} == {
        "tads",
        "reconos",
        "fadereach",
        "fdse",
        "domain_adapter",
    }
    assert all(item.contract_version == "1.0.0" for item in contracts)
    assert IntegrationContract(consumer="custom", purpose="test").consumer == "custom"
