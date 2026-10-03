# ADR 0002 — Final Forensic Hardening

## Status

Accepted — 2026-10-03

## Context

SDEA completed its planned S0–S8 implementation sequence. A repository-wide audit was then performed because passing linting, typing and unit tests does not by itself guarantee semantic correctness.

The audit covered:

- canonical domain models and invariants;
- entity and evidence semantics;
- signal normalization and deduplication;
- fusion and temporal reasoning;
- epistemic state and calibration;
- capability ontology integrity;
- opportunity lifecycle and qualification;
- acquisition recommendation boundaries;
- outcomes and evaluation;
- contract versioning and serialization;
- integrations;
- governance and observability;
- documentation/implementation consistency.

External engineering guidance was also checked against the repository's contract and observability design. OpenTelemetry treats event names, timestamps, attributes and schema evolution as explicit contracts, while NIST AI RMF emphasizes continuous governance, measurement and management rather than treating model output as self-validating.

## Decision

The final repository hardening pass adopts the following permanent rules:

1. Canonical timestamps are timezone-aware.
2. Evidence-backed objects must preserve minimum required lineage.
3. Entity resolution is conservative: ambiguous exact-normalized matches are rejected.
4. Capability ontologies reject unknown parents and cycles.
5. Contract versions are validated before compatibility decisions.
6. Observability events use stable names and explicit schema identity.
7. Governance classification is monotonic: a destination must have sufficient clearance for source sensitivity.
8. SDEA policy controls are recommendation-quality gates only; they are not authorization.
9. Opportunity qualification requires active lifecycle, qualified/confirmed epistemic state, evidence and rationale.
10. Lifecycle transitions are explicit, including retraction.
11. Regression benchmarks are executable and deterministic.
12. Human approval remains mandatory for canonical acquisition recommendations.

## Ownership boundary

SDEA remains a semantic/intelligence library. It does not become a second runtime, authorization system, CRM, outreach engine, crawler, engineering executor or persistence platform.

Authentication, authorization, approvals, secrets, budgets, sandboxing, execution and authoritative audit remain external responsibilities. Tinlance Agent Platform remains the authoritative governed-execution layer.

## Consequences

The repository is safer to integrate because weak or ambiguous inputs fail explicitly rather than being silently promoted into authoritative-looking intelligence. Contract evolution is more predictable, temporal reasoning is less vulnerable to timezone errors, and documentation now matches the implemented repository surface.

Future work should add data/source coverage, calibration datasets, domain-specific adapters and production integrations without weakening these invariants.
