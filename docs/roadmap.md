# SDEA Roadmap

SDEA is a permanent intelligence substrate. Delivery prioritizes semantic correctness, evidence quality, stable contracts, evaluation and explicit ownership boundaries before broad automation.

## Delivery law

Every phase follows:

```
contract → implementation → tests → evaluation → documentation → integration
```

A phase is complete only when its implementation, tests, documentation and CI/workflow are green.

## Final status

**S0–S8 are complete. The repository-wide forensic hardening pass is also complete.**

| Phase | Scope | Status |
|---|---|---|
| S0 | Foundation, domain contracts, invariants, ADRs and CI | Complete |
| S1 | Entity + evidence foundation | Complete |
| S2 | Signal intelligence + adapters | Complete |
| S3 | Fusion + temporal + epistemics | Complete |
| S4 | Capability intelligence + inference | Complete |
| S5 | Opportunity + acquisition intelligence | Complete |
| S6 | Outcomes + evaluation | Complete |
| S7 | Versioned contracts + ecosystem integrations | Complete |
| S8 | Governance + observability + policy foundation | Complete |
| Final forensic hardening | Cross-repository semantic, contract, invariant, documentation and regression audit | Complete |

## S0 — Foundation

Delivered:
- permanent SDEA repository boundary
- canonical immutable Pydantic contracts
- domain invariants
- acquisition-mode taxonomy
- ADR and architecture documentation
- Python 3.12–3.14 CI with Ruff, strict MyPy, pytest and coverage

## S1 — Entity + Evidence Foundation

Delivered:
- canonical entity identity and aliases
- deterministic entity normalization/resolution
- ambiguity-safe entity matching
- epistemic/lifecycle state separation
- timezone-aware chronology validation
- evidence provenance contracts
- deterministic evidence fingerprinting
- source reliability metadata

## S2 — Signal Intelligence

Delivered:
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

## S3 — Fusion + Temporal + Epistemics

Delivered:
- signal correlation and clustering
- source-diversity weighting
- contradiction representation
- temporal intervals, recency, persistence and acceleration
- decay and buying-window derivation
- uncertainty and confidence calibration
- fusion explanations and graph contracts
- timezone-safe temporal primitives

## S4 — Capability Intelligence

Delivered:
- capability ontology and taxonomy
- aliases and relationships
- versioned capability contracts
- parent-integrity and cycle checks
- demand hypotheses
- capability mapping/inference abstraction
- replaceable model gateway
- explainability
- uncertainty and calibration

Models remain replaceable inference components; they do not become domain authority.

## S5 — Opportunity Intelligence

Delivered:
- opportunity graph
- evidence-backed qualification
- explicit lifecycle transitions
- buying windows
- opportunity decay
- acquisition-mode recommendations
- explanation contracts
- downstream handoff contracts
- mandatory human approval on canonical recommendations

SDEA recommends; it does not execute outreach, contracting or engineering work.

## S6 — Closed-Loop Intelligence

Delivered:
- outcome events
- outcome attribution
- feedback labels
- outcome-rate/improvement primitives
- precision/recall metrics
- Brier calibration
- deterministic regression cases
- benchmark registry
- regression evaluation
- human adjudication contracts

The objective is to measure whether intelligence was useful, not merely whether signals were collected.

## S7 — Contracts + Ecosystem Integration

Delivered:
- versioned serialization contracts
- JSON Schema generation
- strict contract-version validation
- major-version compatibility rules
- versioned event contracts
- TADS integration contract
- ReconOS input contract
- FadeReach opportunity handoff contract
- FDSE/FDE handoff contract
- domain-adapter integration contract

External systems may consume or provide intelligence but cannot redefine SDEA semantics or grant SDEA execution authority.

## S8 — Enterprise Hardening

Delivered:
- data classification
- safe sharing semantics
- retention-policy primitives
- deterministic email redaction
- SDEA observability event contracts
- stable observability naming
- schema URL/version identity
- trace-context validation
- recommendation-quality policy controls
- explicit non-authorization boundary

SDEA does not implement its own runtime authorization, secrets, execution budgets, tenant enforcement, persistence engine or infrastructure rate limiter. Those responsibilities remain with the consuming/deployment systems—most importantly Tinlance Agent Platform where governed execution is involved.

## Final forensic hardening

The repository-wide audit repaired issues that ordinary CI could not guarantee:

- canonical timestamps are timezone-aware;
- core evidence-backed objects cannot be constructed without required lineage;
- entity resolution refuses ambiguous matches;
- capability parent relationships are validated and acyclic;
- contract versions are validated before compatibility checks;
- observability events have stable names and explicit schema identity;
- governance sharing semantics no longer permit unsafe downward classification;
- policy decisions are explicitly advisory rather than authorization;
- opportunity qualification checks lifecycle, epistemic state, evidence and rationale;
- lifecycle transitions include explicit retraction paths;
- outcome and adjudication contracts validate required metadata;
- regression benchmarks are executable rather than decorative;
- tests cover the repaired invariants;
- README, architecture, domain-model and roadmap documentation are reconciled with the actual repository surface.

## Permanent anti-roadmap

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

Schema evolution remains explicit and versioned. OpenTelemetry's schema model demonstrates why producers and consumers need stable version identity and explicit evolution rules. urlOpenTelemetry Telemetry Schemashttps://opentelemetry.io/docs/specs/otel/schemas/

SDEA's model/inference boundary also follows the broader risk-management principle that evaluation, governance and measurement should remain continuous rather than treating model output as self-validating. NIST's AI RMF organizes this work across Govern, Map, Measure and Manage. urlNIST AI Risk Management Frameworkhttps://www.nist.gov/itl/ai-risk-management-framework

Future work is therefore evolutionary: new evidence adapters, domain taxonomies, calibration datasets, production integrations and operational deployment—not reopening the SDEA boundary.
