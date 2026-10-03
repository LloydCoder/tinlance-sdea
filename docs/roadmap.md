# Roadmap

SDEA is built as a permanent intelligence substrate. The roadmap therefore prioritizes **semantic correctness, evidence quality and stable contracts before broad automation**.

## Delivery law

Every milestone follows:

```text
contract → implementation → tests → evaluation → documentation → integration
```

No milestone is considered complete merely because code exists. It must be internally testable and documented.

---

## M0 — Foundation

**Objective:** establish the permanent repository boundary and canonical domain language.

### Delivered foundation

- permanent SDEA repository
- domain package
- canonical Pydantic contracts
- evidence/demand invariants
- acquisition-mode taxonomy
- architecture and domain documentation
- ADR discipline
- CI with linting, formatting, typing and coverage

### Exit criteria

- canonical contracts are documented
- invariants have tests
- CI is reproducible across supported Python versions
- ownership boundaries are explicit
- no downstream system's authority is duplicated

---

## M1 — Signal foundation

**Objective:** convert heterogeneous organizational observations into stable, provenance-aware signals.

### Work

- signal normalization contract
- source-adapter interface
- source reliability metadata
- provenance references
- deterministic identity/fingerprinting
- deduplication
- canonical signal taxonomy
- event timestamps versus observation timestamps
- source-specific adapters without source-specific semantics leaking into the domain

### Exit criteria

- the same source event does not create uncontrolled duplicate signals
- signal identity is deterministic enough for reconciliation
- every normalized signal can trace to supporting evidence
- adapters can be added without changing core domain semantics

---

## M2 — Evidence and fusion

**Objective:** turn individual signals into evidence-backed change patterns.

### Work

- evidence relationship model
- signal correlation
- clustering
- source diversity
- contradiction representation
- duplicate/derivative-source detection
- temporal windows
- evidence-weighting policy
- fusion provenance

### Exit criteria

- fused results explain which evidence contributed
- copied versions of one event are not treated as independent corroboration
- contradictory observations remain visible
- temporal relationships are reproducible

---

## M3 — Demand and capability inference

**Objective:** infer plausible capability demand without presenting inference as fact.

### Work

- demand-hypothesis lifecycle
- capability ontology
- capability normalization
- title-to-capability decoding
- capability relationships
- inference strategies
- confidence calibration
- explanation generation
- unknown/insufficient-evidence outcomes

### Exit criteria

- hypotheses are falsifiable
- capability mappings are versioned
- confidence can be evaluated against labeled cases
- insufficient evidence produces uncertainty rather than fabricated certainty
- model-assisted reasoning remains replaceable

---

## M4 — Opportunity intelligence

**Objective:** turn evidence-backed capability demand into qualified opportunity intelligence.

### Work

- opportunity graph
- buying-window derivation
- opportunity lifecycle
- opportunity decay
- qualification rules
- acquisition-mode recommendations
- opportunity explanations
- downstream handoff contract

### Exit criteria

- every opportunity is evidence-traceable
- buying windows expose uncertainty
- stale opportunities can decay without deletion of history
- acquisition recommendations are advisory
- no outreach or execution occurs inside SDEA

---

## M5 — Integrations

**Objective:** connect SDEA to the Tinlance ecosystem through explicit contracts.

### Integrations

- **TADS** — primary product/workflow consumer
- **ReconOS** — reconnaissance and enrichment input
- **FadeReach** — commercial engagement handoff
- **FDSE/FDE** — engineering-delivery handoff
- **Domain adapters** — reusable signal ingestion interfaces

### Exit criteria

- integration contracts are versioned
- failures do not corrupt canonical intelligence
- retries are idempotent where appropriate
- external systems cannot silently redefine SDEA semantics
- no integration grants SDEA hidden execution authority

---

## M6 — Evaluation and enterprise hardening

**Objective:** make SDEA measurable, auditable and production-ready.

### Evaluation

- curated benchmark cases
- signal normalization accuracy
- evidence traceability
- deduplication precision
- contradiction handling
- demand inference precision/recall
- capability mapping accuracy
- confidence calibration
- opportunity qualification quality
- buying-window usefulness
- downstream commercial outcome measurement

### Hardening

- structured audit trail
- policy enforcement
- observability
- dependency/supply-chain controls
- secret management
- tenant isolation where required
- retention/deletion controls
- cost controls
- rate limits
- provenance integrity
- model/provider abstraction
- reproducible evaluation

### Exit criteria

- critical inference paths are benchmarked
- quality regressions are detectable in CI or scheduled evaluation
- important decisions can be reconstructed from evidence
- operational failures are observable
- enterprise boundaries are explicit and testable

---

## Future extensions

These are **post-M6 possibilities**, not commitments to implement them prematurely:

- continuous opportunity monitoring
- cross-domain capability graphs
- market-level demand patterns
- account-level temporal state
- learning from accepted/rejected opportunities
- outcome-aware calibration
- scenario simulation
- customer-specific policy overlays
- sector-specific ontologies
- privacy-preserving intelligence sharing

Future extensions must preserve the core distinction between observation, evidence, inference and action.

## Anti-roadmap

The following are explicitly not roadmap objectives for SDEA:

- becoming a CRM
- building a generic crawler platform
- owning outbound messaging
- executing customer code
- replacing Agent Platform
- replacing Agent OS
- replacing ReconOS
- replacing TADS
- embedding all commercial workflow logic in the intelligence layer

If a proposed feature pushes SDEA across one of these boundaries, create an ADR before implementation.

## Definition of done

A milestone is complete only when:

1. contracts are documented;
2. implementation is tested;
3. invariants are enforced;
4. evaluation evidence exists where applicable;
5. documentation matches the implementation;
6. CI is green;
7. ownership boundaries remain intact;
8. integration behavior is explicit and recoverable.
