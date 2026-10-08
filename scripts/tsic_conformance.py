#!/usr/bin/env python3
"""Fail-closed SDEA verification against the canonical TSIC adapter."""

from __future__ import annotations

import json
from urllib.request import Request, urlopen

TSIC_REVISION = "eee3c96d0c7d00fa5441d9509873fbc9e7402edd"
RAW_ROOT = (
    f"https://raw.githubusercontent.com/LloydCoder/tinlance-system-integration/{TSIC_REVISION}"
)
REQUIRED = {
    "identity-context",
    "event-envelope",
    "delivery-semantics",
    "trace-context",
    "economic-attribution",
}


def fetch_json(path: str) -> dict:
    request = Request(
        f"{RAW_ROOT}/{path}",
        headers={"Accept": "application/json", "User-Agent": "tinlance-sdea-ci"},
    )
    with urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"TSIC contract fetch failed for {path}: HTTP {response.status}")
        return json.load(response)


def main() -> None:
    manifest = fetch_json("manifests/ecosystem.json")
    adapter = fetch_json("integrations/sdea/adapter.json")
    registry = fetch_json("catalog/contracts/registry.json")

    system = next(item for item in manifest["systems"] if item["id"] == "sdea")
    assert system["repository"] == "LloydCoder/tinlance-sdea"
    assert system["governance_role"] == "engineering_acquisition_authority"
    assert adapter["source_system"] == "tsic"
    assert adapter["target_system"] == "sdea"
    assert adapter["status"] == "reference-contract"

    bindings = {item["tsic_contract"] for item in adapter["contract_bindings"]}
    assert bindings == REQUIRED
    assert {item["id"] for item in registry["contracts"]} >= REQUIRED

    authority = adapter["authority"]
    assert authority["integration_contracts"] == "tsic"
    assert authority["engineering_acquisition"] == "sdea"
    assert authority["execution_authority"] == "agent-platform"

    required_invariants = {
        "sdea_is_advisory",
        "recommendation_is_not_action",
        "signal_is_not_evidence",
        "evidence_is_not_demand",
        "job_posting_is_not_the_only_signal_class",
        "tenant_context_is_immutable",
        "tsic_remains_integration_authority",
        "agent-platform_remains_execution_authority",
    }
    assert set(adapter["invariants"]) == required_invariants
    print(f"PASS SDEA TSIC conformance: revision={TSIC_REVISION} contracts={len(bindings)}")


if __name__ == "__main__":
    main()
