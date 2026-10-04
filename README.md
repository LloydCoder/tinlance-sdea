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

These principles align with established engineering practice around explicit semantic conventions and event modeling, and with risk-management guidance emphasizing validity, reliability, transparency, explainability and human oversight. [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

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

- `EpistemicState`
- `LifecycleState`
- `EvidenceState` (compatibility alias)
- `AcquisitionMode`
- `SourceType`

The Python contracts use Pydantic v2, frozen models and forbidden extra fields to make accidental schema drift visible early.

## Repository structure

The repository now contains the complete S0–S8 architecture plus a final forensic hardening pass. The packages are intentionally separated by semantic ownership:

```text
tinlance-sdea/
├── docs/                 # architecture, domain, roadmap and ADRs
├── src/tinlance_sdea/
│   ├── domain/           # canonical immutable contracts + invariants
│   ├── entity/           # canonical identity and ambiguity-safe resolution
│   ├── evidence/         # provenance, fingerprints and reliability
│   ├── signals/          # taxonomy, normalization and deduplication
│   ├── adapters/         # source-adapter extension contracts
│   ├── fusion/           # correlation, clustering, contradiction and graphing
│   ├── temporal/         # recency, persistence, acceleration, decay and windows
│   ├── epistemics/       # confidence, uncertainty, contradiction and calibration
│   ├── capability/       # ontology, taxonomy and capability mappings
│   ├── inference/        # demand/capability inference abstractions
│   ├── opportunity/      # qualification, lifecycle, buying windows and handoff
│   ├── acquisition/      # advisory acquisition-mode recommendations
│   ├── outcomes/         # outcome events, attribution and feedback
│   ├── evaluation/       # metrics, benchmarks, regression and adjudication
│   ├── contracts/        # versioned serialization/schema/event contracts
│   ├── governance/       # classification, retention and redaction primitives
│   ├── observability/    # SDEA semantic conventions and trace context
│   ├── policy/           # non-authoritative recommendation-quality gates
│   └── integrations/     # TADS, ReconOS, FadeReach, FDSE and adapter contracts
├── tests/                # phase and invariant regression coverage
├── pyproject.toml
└── .github/workflows/    # Python 3.12–3.14 CI
```

All planned implementation phases S0–S8 are complete. The final hardening pass tightened semantic invariants, timezone discipline, entity ambiguity handling, ontology integrity, contract version validation, governance semantics, observability schema identity, lifecycle transitions and regression evaluation.

## Engineering invariants

The completed implementation enforces these invariants:

- Evidence and signals use timezone-aware observation/collection timestamps.
- Signals, hypotheses and opportunities retain evidence lineage.
- Demand hypotheses require supporting signals and explicit rationale.
- Opportunities require evidence and explicit rationale.
- Confidence, urgency and reliability remain bounded from 0 to 1.
- Canonical models reject unexpected fields and are immutable after construction.
- Entity resolution rejects ambiguous exact-normalized matches rather than silently selecting one.
- Capability ontology parent relationships are validated and acyclic.
- Contract versions are validated and compatibility is explicitly major-version based.
- Observability events use stable names and versioned schema identity.
- Opportunity lifecycle transitions are explicit and auditable.
- Acquisition recommendations cannot disable human approval.
- SDEA policy decisions are advisory quality gates, never authorization.
- Agent Platform remains the authoritative owner of permissions and action approvals.
- Regression benchmarks and calibration metrics are deterministic and inspectable.

## Roadmap

The planned implementation sequence is complete:

| Phase | Scope | Status |
|---|---|---|
| S0 | Foundation, domain contracts, ADRs and CI | Complete |
| S1 | Entity + evidence foundation | Complete |
| S2 | Signal intelligence + adapters | Complete |
| S3 | Fusion + temporal + epistemics | Complete |
| S4 | Capability intelligence + inference | Complete |
| S5 | Opportunity + acquisition intelligence | Complete |
| S6 | Outcomes + evaluation | Complete |
| S7 | Versioned contracts + ecosystem integrations | Complete |
| S8 | Governance + observability + policy hardening | Complete |
| Final forensic hardening | Repository-wide semantic, contract, security and documentation audit | Complete |

Each phase was gated by the repository quality workflow before the next phase was advanced. The final audit then reviewed the complete code/document surface and repaired semantic gaps that ordinary linting, typing and unit tests could not identify.

**Permanent rule:** SDEA remains an intelligence substrate. New integrations must not redefine its core semantics or introduce CRM, outreach, execution or authorization responsibilities.

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

## Production deployment

SDEA has a first-stage VPS deployment profile for a 4 vCPU / 8 GB RAM Linux host:

~~~text
Internet
   |
   v
Caddy :80/:443
   |
   v
SDEA API :8000
   |        \
   v         v
PostgreSQL  Valkey
   ^
   |
SDEA Worker
~~~

The production runtime is containerized and managed with Docker Compose. The application image is published to GitHub Container Registry by GitHub Actions. PostgreSQL and Valkey are private to the Compose network; only Caddy exposes host ports.

The service exposes dependency-aware operational endpoints:

- /healthz — dependency-free liveness
- /readyz — PostgreSQL + Valkey readiness
- /version — deployed version metadata

The VPS runbook is in [docs/deployment](deploy/README.md).

The deployment deliberately does **not** claim that source ingestion, persistence repositories, or inference workers are production-complete. The runtime shell is implemented first; domain handlers are connected only when their contracts, persistence, retries, idempotency and evaluation are implemented and tested.

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

**Planned implementation complete — S0–S8 plus final forensic hardening are complete.**

The repository remains a maintained enterprise-grade intelligence foundation: future work is additive evolution, new source/domain adapters, calibration data, integrations and operational deployment—not reopening the core architectural boundary.

The project is deliberately optimizing for **trustworthy intelligence, durable contracts and architectural clarity before feature volume**.

The long-term objective is not to build another lead scraper. It is to build a reusable intelligence layer that can recognize meaningful organizational change, explain the capability demand it implies, identify when the window may matter, and hand a governed opportunity to the systems responsible for commercial execution.

## License

Proprietary — Tinlance Limited.
