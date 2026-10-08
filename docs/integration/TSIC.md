# TSIC integration

SDEA consumes TSIC's canonical ecosystem contracts while retaining authority over Signal-Driven Engineering Acquisition.

## Boundary

- **TSIC** owns integration contracts, compatibility and ecosystem certification.
- **SDEA** owns signal semantics, fusion, temporal reasoning, demand/capability inference and acquisition recommendations.
- **TADS** owns target/account intelligence.
- **ReconOS** owns deep OSINT enrichment.
- **FadeReach** owns outreach execution.
- **FDSE** owns engineering/transformation delivery.
- **Agent Platform** owns consequential execution authority.

The canonical acquisition sequence is:

`World Intelligence → TADS → SDEA → ReconOS → FadeReach → Sales → FDSE`

A recommendation is not an action. SDEA never grants execution authority.

## Conformance

```bash
python scripts/tsic_conformance.py
```

The gate consumes the immutable TSIC revision declared by the script and verifies the SDEA adapter, contract registry, authority mapping and advisory invariants.

Passing the gate proves reviewed contract compatibility; it does not claim external deployment.
