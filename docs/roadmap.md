# SDEA Roadmap

SDEA is a permanent intelligence substrate. Delivery prioritizes semantic correctness, evidence quality, stable contracts, evaluation and explicit ownership boundaries before broad automation.

## Delivery law

Every phase follows:

```
contract → implementation → tests → evaluation → documentation → integration
```

A phase is complete only when its implementation, tests, documentation and CI/workflow are green.

## S0 — Foundation

**Status: complete.**

Delivered:
- permanent SDEA repository boundary
- canonical Pydantic domain contracts
- domain invariants
- acquisition-mode taxonomy
- ADR and architecture documentation
- Python 3.12–3.14 CI with Ruff, strict MyPy, pytest and coverage

## S1 — Entity + Evidence Foundation

**Status: complete.**

Delivered:
- canonical entity identity and aliases
- deterministic entity normalization/resolution
- epistemic/lifecycle state separation
- chronology validation
- evidence provenance contracts
- deterministic evidence fingerprinting
- source reliability metadata
- S1 tests and documentation reconciliation

Exit condition: an observation can be attached to a canonical entity and its supporting evidence can be traced, fingerprinted and interpreted without conflating certainty with lifecycle.

## S2 — Signal Intelligence

**Status: in progress.**

Objective: convert heterogeneous organizational observations into deterministic, provenance-aware canonical signals.

Work:
- canonical signal taxonomy and version
- normalized signal record
- deterministic normalization
- chronology and evidence validation
- deterministic signal fingerprints
- deduplication
- signal registry
- source-adapter interface
- adapter capabilities and health contracts
- adapter registry
- integration-safe tests

Exit criteria:
- every normalized signal has evidence lineage
- signal identity is deterministic enough for reconciliation
- taxonomy is explicit and versioned
- duplicate source events can be collapsed deterministically
- adapters can be added without changing canonical signal semantics
- CI is green across the supported Python matrix

## S3 — Fusion + Temporal + Epistemics

**Status: in progress.**

Build:
- signal correlation and clustering
- source-diversity weighting
- derivative/copy detection
- contradiction representation
- temporal intervals, recency, persistence and acceleration
- decay and buying-window derivation
- explicit epistemic uncertainty and confidence calibration
- fusion explanations and provenance

Exit: SDEA can explain why multiple observations represent meaningful organizational change without double-counting or hiding contradictions.

## S4 — Capability Intelligence

**Status: in progress.**

Build:
- capability ontology and taxonomy
- aliases and relationships
- capability normalization and versioning
- demand hypotheses
- demand/capability inference strategies
- rule/model gateway
- explainability
- uncertainty and calibration

LLMs or other models remain replaceable inference components; they do not become domain authority.

## S5 — Opportunity Intelligence

Build:
- opportunity graph
- qualification
- lifecycle
- buying windows
- opportunity decay
- acquisition-mode reasoning
- explanation
- downstream handoff contract

SDEA recommends; it does not execute outreach, contracting or engineering work.

## S6 — Closed-Loop Intelligence

Build:
- outcome events
- attribution
- accepted/rejected opportunity feedback
- calibration learning
- curated benchmark cases
- regression tests
- adjudication workflows
- precision/recall and calibration measurement

The objective is to measure whether intelligence was useful, not merely whether signals were collected.

## S7 — Contracts + Ecosystem Integration

Build:
- versioned serialization contracts
- JSON Schema
- compatibility rules
- event contracts
- TADS integration
- ReconOS input contract
- FadeReach opportunity handoff
- FDSE/FDE handoff
- domain-adapter integration contracts

External systems may consume or provide intelligence but cannot redefine SDEA semantics or grant SDEA execution authority.

## S8 — Enterprise Hardening

Build:
- provenance integrity and reconstruction
- data classification
- retention/deletion controls
- redaction
- tenant boundaries where required
- SDEA-specific observability
- operational policy controls
- rate/cost controls
- dependency and supply-chain controls
- security testing
- reproducible evaluation
- contract compatibility testing
- production-readiness audit

## Anti-roadmap

SDEA will not become:
- a CRM
- an outreach engine
- a generic crawler/scraper platform
- an account-enrichment replacement for ReconOS
- an agent runtime
- an engineering execution engine
- an authorization/approval authority
- a replacement for TADS, ReconOS, FadeReach, FDSE or Agent Platform

Any feature that crosses a permanent boundary requires an ADR before implementation.

## Definition of done

A phase is complete only when:

1. canonical contracts are documented;
2. implementation is tested;
3. invariants are enforced;
4. relevant evaluation evidence exists;
5. documentation matches the implementation;
6. CI/workflows are green;
7. ownership boundaries remain intact;
8. integration behavior is explicit and recoverable.

Schema evolution must remain explicit and versioned. This follows the general lesson from OpenTelemetry's schema model: producers and consumers need a stable way to evolve contracts without silently breaking interpretation. urlOpenTelemetry Telemetry Schemashttps://opentelemetry.io/docs/specs/otel/schemas/

Provenance should remain rich enough to describe entities, activities, agents and derivations where applicable, consistent with the W3C PROV model. urlW3C PROV publicationshttps://www.w3.org/groups/wg/prov/publications/

Evaluation is a first-class engineering concern. NIST's AI measurement/evaluation guidance emphasizes documented metrics, test sets and repeatable TEVV practices for trustworthy AI systems. urlNIST AI measurement and evaluationhttps://www.nist.gov/ai-measurement-and-evaluation
