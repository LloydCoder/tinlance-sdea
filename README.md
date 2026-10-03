# Tinlance SDEA

**Signal-Driven Engineering Acquisition (SDEA)** is Tinlance's permanent intelligence layer for turning observable organizational change into evidence-backed capability-demand intelligence and commercially actionable opportunities.

SDEA answers a specific question:

> **What is changing inside an organization, what evidence supports that change, what capability demand may follow, why might it matter now, and what is the appropriate way to acquire that capability?**

It is deliberately positioned **between observation and commercial execution**. SDEA does not replace the systems that discover accounts, communicate with prospects, execute engineering work, or govern agent actions.

## The thesis

Organizations rarely announce every future capability need as a clean request. Their behavior leaves a trail:

- hiring and team expansion
- funding and financing
- product launches, releases, pricing or packaging changes
- technology migrations and infrastructure changes
- AI adoption and automation initiatives
- security events and resilience work
- leadership changes
- geographic or market expansion
- partnerships and acquisitions
- procurement, RFP and vendor activity
- regulatory or compliance changes
- open-source activity and technical direction

A job posting is therefore **one signal class among many**, not the definition of SDEA.

The system's job is not to collect the most signals. It is to determine which combinations of signals constitute meaningful, evidence-backed changes and whether those changes plausibly imply a capability need.

## The core distinction

SDEA maintains hard semantic boundaries:

```text
signal        ≠ evidence
evidence      ≠ demand
demand        ≠ capability
capability    ≠ opportunity
opportunity   ≠ customer
recommendation ≠ action
```

A signal is a normalized representation of something meaningful that happened or appears to be happening.

Evidence is the underlying observable artifact or observation supporting that signal.

Demand is an interpretation of what capability the organization may need.

Capability is the normalized thing that may be required.

An opportunity is a commercially relevant, evidence-backed capability need with timing and acquisition context.

A customer is a business relationship established outside SDEA.

This separation is foundational: **SDEA must never turn weak observation into false certainty simply because an automated system can produce a plausible narrative.**

## Canonical intelligence pipeline

```text
                    EXTERNAL WORLD
                          │
                    Entity / Event
                          │
                          ▼
                       SIGNAL
                          │
                          ▼
                 EVIDENCE + PROVENANCE
                          │
                          ▼
                  SIGNAL NORMALIZATION
                          │
                          ▼
                  SIGNAL FUSION / CLUSTER
                          │
                          ▼
                 TEMPORAL REASONING
                          │
                          ▼
                 DEMAND HYPOTHESIS
                          │
                          ▼
                  CAPABILITY NEED
                          │
                          ▼
                     OPPORTUNITY
                  ┌───────┼────────┐
                  │       │        │
             confidence why-now buying-window
                  │       │        │
                  └───────┼────────┘
                          ▼
              ACQUISITION RECOMMENDATION
                          │
                          ▼
                 HUMAN-APPROVED ACTION
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          FadeReach     FDE/AaaS     Product
             │            │            │
             └────────────┼────────────┘
                          ▼
                    CUSTOMER OUTCOME
                          │
                          └──────► NEW SIGNALS
```

The most important architectural boundary is the final one: **SDEA recommends; downstream systems and humans decide and act.**

## What SDEA owns

SDEA permanently owns the intelligence semantics required to move from organizational change to capability demand:

| Capability | SDEA responsibility |
|---|---|
| Signal semantics | Define, normalize and version signal types |
| Evidence | Preserve supporting artifacts, timestamps and provenance |
| Fusion | Correlate multiple signals and identify clusters |
| Temporal reasoning | Model recency, persistence, emergence, staleness and decay |
| Uncertainty | Preserve unknown, contradictory, partial and hypothesized states |
| Demand inference | Form falsifiable demand hypotheses |
| Capability inference | Translate demand into normalized capability needs |
| Capability ontology | Maintain reusable capability vocabulary and relationships |
| Opportunity intelligence | Qualify evidence-backed commercial opportunities |
| Buying windows | Represent when a capability need may be actionable |
| Acquisition intelligence | Compare plausible acquisition modes without executing them |
| Explainability | Preserve why an inference or recommendation exists |
| Evaluation | Measure inference quality, calibration and outcome usefulness |
| Integration contracts | Define stable interfaces to consuming/producing systems |

## What SDEA does not own

SDEA is **not**:

- a CRM
- an outreach platform
- a generic web scraper
- an account-enrichment system
- an agent runtime
- an engineering execution engine
- a GitHub execution layer
- a source of authorization
- a system that autonomously contacts prospects
- a system that silently converts model output into commercial truth

Those boundaries are intentional and permanent.

## Tinlance system boundary

```text
                  ┌──────────────────────────────┐
                  │        External World         │
                  └──────────────┬───────────────┘
                                 │
                    sources / domain adapters
                                 │
          ┌──────────────────────▼──────────────────────┐
          │                    SDEA                      │
          │                                              │
          │ Signal → Evidence → Fusion → Demand         │
          │        → Capability → Opportunity            │
          │        → Buying Window → Recommendation      │
          └──────────────────────┬───────────────────────┘
                                 │
                         opportunity contract
                                 │
              ┌──────────────────▼──────────────────┐
              │       Tinlance commercial layer     │
              │ TADS / ReconOS / FadeReach / FDE   │
              └──────────────────┬──────────────────┘
                                 │
                         governed execution
                                 │
                    Agent Platform / Agent OS
```

### Permanent ownership boundaries

| System | Primary responsibility |
|---|---|
| **SDEA** | Signal semantics, evidence/provenance, fusion, temporal reasoning, demand/capability inference, opportunity intelligence and acquisition recommendations |
| **TADS** | Demand-intelligence product experience, account workflows and operational consumption of SDEA intelligence |
| **ReconOS** | Deep account/company reconnaissance and enrichment |
| **FadeReach** | Engagement, outreach and conversion workflows |
| **FDSE / FDE** | Engineering execution, delivery and engineering-domain workflows |
| **Agent Platform** | Authoritative identity, authorization, approvals, runtime, tools/MCP, sandbox, budgets, evidence, audit and observability |
| **Agent OS** | Higher-level agent/workspace lifecycle, orchestration environment and operating experience |

The dependency direction is:

```text
TADS / ReconOS / Domain Adapters
                │
                ▼
               SDEA
                │
                ▼
           Opportunity
                │
                ▼
            FadeReach
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
       FDE     AaaS    Product
        │       │        │
        └───────┼────────┘
                ▼
        Customer outcome
                │
                └──────► SDEA feedback
```

SDEA may consume intelligence from upstream systems and publish intelligence downstream, but it does not inherit their authority.

## Acquisition modes

SDEA can represent multiple ways an organization may acquire a capability:

| Mode | Meaning |
|---|---|
| **Hire** | Add internal employees |
| **Build** | Develop internally |
| **Buy** | Purchase an external product/platform |
| **Partner** | Engage an external specialist or strategic partner |
| **Fractional** | Obtain fractional expertise |
| **FDE** | Use embedded/fractional delivery engineering |
| **Project** | Commission bounded implementation work |
| **Managed service** | Outsource an ongoing operational capability |
| **AaaS** | Acquire an agent/AI workforce capability as a service |
| **Product** | Acquire a Tinlance product capability |

The recommendation layer is advisory. It does not decide which mode a customer must choose.

## Evidence-first operating principles

1. **Evidence before inference.** Consequential conclusions must be traceable to evidence.
2. **Provenance is part of meaning.** Source, collection time and observation time matter.
3. **Uncertainty is data.** Unknown, partial, conflicting and hypothesized states must remain representable.
4. **Temporal context matters.** A signal without time can be commercially misleading.
5. **Corroboration beats volume.** Independent supporting evidence is more useful than repeated copies of the same source.
6. **Recommendations are not actions.** SDEA produces intelligence; downstream systems perform approved actions.
7. **Models are replaceable.** Domain contracts must not depend on one LLM, classifier or vendor.
8. **Outcomes beat signal counts.** More signals do not necessarily mean better intelligence.
9. **No hidden authority.** SDEA cannot grant permissions, approve actions or execute customer changes.
10. **Every important conclusion should be explainable.** A consumer should be able to understand what changed, what supports it and why the inference exists.

These principles align with established engineering practice around explicit semantic conventions and event modeling, and with risk-management guidance emphasizing validity, reliability, transparency, explainability and human oversight. urlOpenTelemetry semantic conventionshttps://opentelemetry.io/docs/concepts/semantic-conventions/ urlNIST AI Risk Management Frameworkhttps://www.nist.gov/itl/ai-risk-management-framework

## Canonical domain contracts

The current domain layer establishes these core contracts:

- `Evidence`
- `Signal`
- `SignalCluster`
- `DemandHypothesis`
- `CapabilityNeed`
- `BuyingWindow`
- `Opportunity`
- `AcquisitionRecommendation`

The canonical enums currently include:

- `EvidenceState`
- `AcquisitionMode`
- `SourceType`

The Python contracts use Pydantic v2, frozen models and forbidden extra fields to make accidental schema drift visible early.

## Repository structure

The repository intentionally separates **implemented foundations** from **future architectural boundaries**:

```text
tinlance-sdea/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── adr/
│   │   ├── README.md
│   │   └── 0001-sdea-boundary.md
│   ├── architecture.md
│   ├── domain-model.md
│   └── roadmap.md
├── src/
│   └── tinlance_sdea/
│       ├── domain/          # canonical contracts + invariants
│       ├── evidence/        # evidence lifecycle boundary
│       ├── signals/         # signal semantics + normalization
│       ├── fusion/          # correlation and signal clustering
│       ├── temporal/        # time-aware reasoning
│       ├── inference/       # demand/capability inference
│       ├── opportunity/     # opportunity intelligence
│       ├── acquisition/     # acquisition-mode intelligence
│       ├── policy/          # SDEA decision/policy constraints
│       └── integrations/    # external system contracts
├── tests/
│   └── test_domain_models.py
├── pyproject.toml
├── .pre-commit-config.yaml
└── README.md
```

The package directories beyond `domain/` are architectural seams; they do not imply that every subsystem is already implemented.

## Engineering invariants

The current foundation enforces or documents these invariants:

- An opportunity must remain traceable to evidence.
- A demand hypothesis requires an explicit rationale.
- Confidence values remain bounded from 0 to 1.
- Canonical models reject unexpected fields.
- Canonical models are immutable after construction.
- Recommendations require human approval by default.
- SDEA does not own execution authority.

Future invariants will cover provenance integrity, temporal consistency, contradiction handling, deduplication, confidence calibration and integration contracts.

## Roadmap

SDEA is intentionally built in controlled milestones.

### M0 — Foundation
**Current foundation:** repository boundary, canonical domain contracts, invariants, documentation, ADR discipline and CI quality gates.

### M1 — Signal foundation
Normalize heterogeneous sources into stable signal contracts; add source adapters, provenance references, deduplication and source reliability metadata.

### M2 — Evidence and fusion
Build evidence relationships, signal clustering, correlation, contradiction handling and temporal reasoning.

### M3 — Demand and capability inference
Introduce demand hypotheses, capability ontology, capability inference, explainability and confidence calibration.

### M4 — Opportunity intelligence
Introduce opportunity qualification, buying windows, opportunity decay and acquisition-mode recommendations.

### M5 — Integrations
Connect TADS, ReconOS, FadeReach, FDSE/FDE and domain-specific signal adapters through explicit versioned contracts.

### M6 — Evaluation and enterprise hardening
Add benchmark cases, precision/recall analysis, calibration, auditability, observability, policy controls, cost controls and multi-tenant boundaries where required.

**Rule:** each milestone must leave the repository testable, documented and internally coherent. New integrations must not be allowed to redefine SDEA's core semantics.

## Development

Requirements: Python 3.12+.

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the local quality gates:

```ruff check .
ruff format --check .
mypy src
pytest --cov=tinlance_sdea --cov-report=term-missing
```

CI currently tests Python 3.12, 3.13 and 3.14 and applies linting, formatting, strict typing and coverage gates.

## Security and trust

SDEA is intended to process potentially sensitive business intelligence. Enterprise hardening therefore needs to address:

- provenance integrity
- source and collection metadata
- secret handling
- dependency and supply-chain security
- tenant isolation where deployed multi-tenant
- access control at consuming systems
- auditability of inference and recommendation changes
- retention and deletion policies
- protection against poisoned or misleading source material
- prompt/model manipulation where LLMs participate in inference
- reproducible evaluation of inference quality

SDEA's intelligence layer must never be treated as an authorization boundary.

## Documentation

- [Architecture](docs/architecture.md)
- [Domain Model](docs/domain-model.md)
- [Roadmap](docs/roadmap.md)
- [Architecture Decision Records](docs/adr/README.md)
- [Permanent boundary ADR](docs/adr/0001-sdea-boundary.md)

## Project status

**Active development — M0 foundation.**

The project is deliberately optimizing for **trustworthy intelligence, durable contracts and architectural clarity before feature volume**.

The long-term objective is not to build another lead scraper. It is to build a reusable intelligence layer that can recognize meaningful organizational change, explain the capability demand it implies, identify when the window may matter, and hand a governed opportunity to the systems responsible for commercial execution.

## License

Proprietary — Tinlance Limited.
