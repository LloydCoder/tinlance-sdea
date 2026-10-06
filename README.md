# Tinlance SDEA

**Signal-Driven Engineering Acquisition (SDEA) is an evidence-backed intelligence layer for teams that need to detect emerging organizational capability demand, explain why it matters now, and hand qualified opportunities to downstream systems.**

[![CI](https://github.com/LloydCoder/tinlance-sdea/actions/workflows/ci.yml/badge.svg)](https://github.com/LloydCoder/tinlance-sdea/actions/workflows/ci.yml)
[![Container](https://github.com/LloydCoder/tinlance-sdea/actions/workflows/container.yml/badge.svg)](https://github.com/LloydCoder/tinlance-sdea/actions/workflows/container.yml)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-proprietary-lightgrey)](LICENSE)

## Visual proof

The canonical pipeline is explicit and auditable:

```text
External world
     │
     ▼
Entity / Event → Signal → Evidence + Provenance
                         │
                         ▼
                  Signal Fusion
                         │
                         ▼
                 Temporal Reasoning
                         │
                         ▼
                 Demand Hypothesis
                         │
                         ▼
                 Capability Need
                         │
                         ▼
                    Opportunity
                  ┌──────┼──────┐
                  ▼      ▼      ▼
              confidence why-now buying-window
                         │
                         ▼
              Acquisition Recommendation
                         │
                         ▼
                 Human-approved action
```

> [!NOTE]
> This repository currently publishes the intelligence contracts and Python implementation rather than a hosted interactive demo. A real demo GIF or hosted walkthrough should be added when one is available; this README does not fabricate one.

## Why SDEA

SDEA is intentionally narrower than a sales or automation platform.

| SDEA | Not SDEA |
|---|---|
| Signal semantics and normalization | CRM |
| Evidence and provenance | Generic scraper |
| Signal fusion and temporal reasoning | Account-enrichment replacement |
| Demand and capability inference | Outreach engine |
| Opportunity intelligence | Engineering execution engine |
| Acquisition recommendations | Authorization or approval authority |
| Evaluation and calibration | Autonomous commercial action |

The core semantic boundary is:

**signal ≠ evidence ≠ demand ≠ capability ≠ opportunity ≠ customer; recommendation ≠ action.**

A job posting is only one signal class. SDEA can represent hiring, funding, product changes, technology migrations, AI adoption, security events, leadership changes, expansion, partnerships, procurement, regulation and open-source activity.

## Quick Start

Prerequisite: Python 3.12+.

```bash
git clone https://github.com/LloydCoder/tinlance-sdea.git
cd tinlance-sdea
python -m pip install -e ".[dev]"
python -c "import tinlance_sdea; print(tinlance_sdea.__version__)"
pytest -q
```

The final command exercises the repository test suite. The package version currently reports `0.1.0`.

## Installation

### Development

```bash
python -m pip install -e ".[dev]"
```

### Runtime package

```bash
python -m pip install .
```

### Container

A production-oriented Docker/Compose profile is provided under [deploy/](deploy/). It includes the SDEA API, worker, PostgreSQL, Valkey and Caddy topology.

> [!WARNING]
> The deployment shell is not a claim that every ingestion, persistence or inference workflow is production-complete. Read [deploy/README.md](deploy/README.md) before deployment.

## Usage

SDEA exposes typed Python contracts rather than a vendor-specific prompt or crawler API.

Basic package verification:

```python
import tinlance_sdea

print(tinlance_sdea.__version__)
```

The canonical domain contracts live under [src/tinlance_sdea/domain/](src/tinlance_sdea/domain/). Signal normalization, evidence, fusion, temporal reasoning, capability inference, opportunity intelligence, evaluation, governance and integrations are separated by semantic ownership.

For API/runtime work, inspect [src/tinlance_sdea/service/](src/tinlance_sdea/service/) and the deployment profile before integrating.

## Configuration

| Area | Default / contract | Notes |
|---|---|---|
| Python | 3.12+ | CI covers 3.12, 3.13 and 3.14 |
| Package version | 0.1.0 | Defined in `src/tinlance_sdea/__init__.py` |
| Line length | 100 | Ruff |
| Type checking | strict MyPy | `src/` |
| Coverage gate | 90% | Branch coverage |
| Deployment DB | PostgreSQL | Private Compose network |
| Deployment queue/cache | Valkey | Private Compose network |
| Deployment proxy | Caddy | Public HTTP/HTTPS edge |
| Recommendation approval | Required | SDEA remains advisory |

## Features

| Capability | Status |
|---|---|
| Immutable Pydantic v2 domain contracts | Implemented |
| Entity normalization and ambiguity-safe resolution | Implemented |
| Evidence provenance and deterministic fingerprints | Implemented |
| Versioned signal taxonomy and deduplication | Implemented |
| Signal fusion, contradiction and source-diversity handling | Implemented |
| Temporal reasoning, decay and buying windows | Implemented |
| Capability ontology and demand inference abstractions | Implemented |
| Opportunity qualification and lifecycle | Implemented |
| Acquisition-mode recommendations | Implemented |
| Outcome evaluation and calibration primitives | Implemented |
| Versioned integration/event contracts | Implemented |
| Governance, redaction and observability contracts | Implemented |
| TADS / ReconOS / FadeReach / FDSE integration contracts | Implemented |
| Hosted interactive demo | Not currently published |

## Documentation

- [Documentation index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Domain model](docs/domain-model.md)
- [Roadmap and definition of done](docs/roadmap.md)
- [Architecture Decision Records](docs/adr/README.md)
- [Deployment runbook](deploy/README.md)
- [LLM context](llms.txt)

## Development

Run the same local gates used by CI:

```bash
ruff check .
ruff format --check .
mypy src
pytest --cov=tinlance_sdea --cov-report=term-missing
```

CI covers Python 3.12–3.14. Container builds are validated separately by GitHub Actions.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Changes to SDEA's permanent ownership boundaries require an ADR.

## Support and security

- General support: [SUPPORT.md](SUPPORT.md)
- Security reporting: [SECURITY.md](SECURITY.md)
- Community standards: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## License

Tinlance SDEA is proprietary software owned by Tinlance Limited. See [LICENSE](LICENSE).

## Acknowledgements

SDEA's engineering discipline draws on established practices including Pydantic's typed validation model, OpenTelemetry semantic conventions and NIST AI risk-management concepts. These references inform engineering decisions; they do not imply endorsement or certification.
