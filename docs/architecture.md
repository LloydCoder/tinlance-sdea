# SDEA Architecture

## 1. Mission

SDEA converts externally observable organizational change into evidence-backed capability-demand intelligence and qualified acquisition opportunities.

The architectural objective is not maximum data collection. It is a trustworthy chain of reasoning:

```text
observable change
→ normalized signal
→ supporting evidence
→ correlated signal cluster
→ temporal interpretation
→ demand hypothesis
→ capability need
→ opportunity
→ buying window
→ acquisition recommendation
```

## 2. Architectural position

SDEA sits between **organizational observation** and **commercial execution**.

It is a shared intelligence layer rather than a product-specific workflow engine.

```text
External sources / domain adapters
              │
              ▼
        ┌─────────────┐
        │    SDEA     │
        │ intelligence│
        └──────┬──────┘
               │
               ▼
        Commercial systems
   TADS / FadeReach / FDE / AaaS
               │
               ▼
       Governed execution
   Agent Platform / Agent OS
```

SDEA can receive normalized inputs from TADS, ReconOS and domain adapters. It should not make those systems depend on SDEA for unrelated responsibilities.

## 3. Canonical pipeline

### Stage 1 — Entity / Event

A source reports an observable occurrence associated with an organization or other entity.

Examples:

- a new engineering team appears
- a company announces a market expansion
- a production platform migration is disclosed
- a security event is reported
- a new AI initiative is announced
- a procurement event becomes visible

### Stage 2 — Signal

The occurrence is normalized into a stable signal contract.

A signal should answer:

- what changed?
- for which entity?
- when did it occur?
- when was it observed?
- what type of change is it?
- which evidence supports it?

### Stage 3 — Evidence + provenance

Evidence records the underlying artifact or observation and its provenance.

At minimum, the architecture should preserve:

- source type
- source reference where available
- observed time
- collected time
- title/context
- optional excerpt
- content hash where appropriate
- provenance reference
- source-specific metadata

Observation time and collection time are intentionally distinct. This prevents a late collection from being mistaken for a recent event.

### Stage 4 — Signal fusion

Independent signals may provide stronger evidence together than individually.

Fusion should:

- correlate signals by entity
- consider temporal proximity
- identify repeated or derivative copies
- preserve source diversity
- represent contradiction
- avoid double-counting the same underlying event

The design goal is **evidence quality, not signal volume**.

### Stage 5 — Temporal reasoning

Demand is time-sensitive.

The temporal layer must eventually distinguish:

- emerging
- active
- accelerating
- delayed
- stale
- decaying
- resolved

A buying window is an uncertainty-bearing interval, not a claimed exact purchase date.

### Stage 6 — Demand hypothesis

A demand hypothesis is a falsifiable interpretation of observed organizational behavior.

It should explain:

- what capability may be needed
- why the evidence supports that interpretation
- how confident the system is
- what remains unknown

It must remain explicitly different from a confirmed customer requirement.

### Stage 7 — Capability need

The system translates a demand hypothesis into normalized capability language.

This enables multiple expressions of the same underlying need to converge on a reusable ontology.

For example, several different job titles may point toward one capability family; the title itself is not the capability model.

### Stage 8 — Opportunity

An opportunity is a commercially relevant capability need that remains evidence-backed.

It should carry:

- entity
- capability need
- supporting evidence
- confidence
- rationale
- acquisition modes
- optional buying window

An opportunity is not a customer and does not authorize engagement.

### Stage 9 — Acquisition recommendation

SDEA may recommend plausible acquisition modes:

```text
Hire | Build | Buy | Partner | Fractional
FDE | Project | Managed Service | AaaS | Product
```

The recommendation is advisory. Commercial systems and humans determine whether and how to act.

## 4. Permanent ownership boundaries

| System | Owns |
|---|---|
| **SDEA** | signal semantics, evidence/provenance, fusion, temporal reasoning, demand/capability inference, opportunity intelligence, acquisition recommendations and evaluation |
| **TADS** | demand-intelligence product experience and workflows |
| **ReconOS** | account/company reconnaissance and enrichment |
| **FadeReach** | engagement and outreach execution |
| **FDSE/FDE** | engineering execution and delivery semantics |
| **Agent Platform** | authoritative identity, authorization, approval, runtime, tools, sandbox, budgets, evidence, audit and observability |
| **Agent OS** | higher-level agent/workspace lifecycle and operating environment |

### Boundary rules

1. SDEA must not become a CRM.
2. SDEA must not own outreach execution.
3. SDEA must not become a generic scraping platform.
4. SDEA must not execute customer engineering work.
5. SDEA must not create a second authorization or approval system.
6. SDEA must not duplicate Agent Platform runtime, sandbox, audit or tool authority.
7. SDEA must not replace ReconOS's deep reconnaissance responsibility.
8. SDEA must not replace TADS's product/workflow layer.
9. SDEA must not turn an inference into a customer fact without evidence.
10. SDEA must not silently trigger commercial action.

## 5. Contract direction

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
       ┌──────┼───────┐
       ▼      ▼       ▼
      FDE    AaaS   Product
       │      │       │
       └──────┼───────┘
              ▼
       customer outcome
              │
              └──────► new observable signals
```

The integration boundary should use explicit versioned contracts. SDEA should publish intelligence, not implicit internal state.

## 6. Data and semantic discipline

SDEA's canonical data path should preserve the distinction between:

- source artifact
- observation
- normalized signal
- inference
- opportunity
- recommendation
- downstream action

This is analogous to established telemetry practice: named events represent distinct occurrences, while structured attributes carry contextual details. OpenTelemetry's semantic-convention guidance also emphasizes stable names, timestamps and documented attributes. [OpenTelemetry events and semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/events/)

SDEA should therefore prefer explicit, versioned schemas over opaque model-generated blobs.

## 7. Trust, safety and evaluation

The system should treat inference quality as an engineering property.

Future evaluation must measure at least:

- evidence traceability
- signal normalization accuracy
- deduplication quality
- contradiction handling
- demand inference precision/recall
- capability mapping quality
- confidence calibration
- buying-window usefulness
- opportunity qualification quality
- downstream commercial outcomes

Model-assisted inference must remain measurable, reviewable and replaceable. NIST's AI RMF emphasizes validity/reliability, accountability/transparency, explainability and ongoing testing/monitoring as trustworthiness concerns; those principles are useful design constraints for SDEA's inference layer. urlNIST AI RMFhttps://www.nist.gov/itl/ai-risk-management-framework

## 8. Current implementation boundary

S0 and S1 implement the canonical domain and entity/evidence foundations. S2 adds deterministic signal intelligence:

- canonical signal taxonomy with explicit version
- normalized signal records
- chronology and evidence validation
- deterministic signal fingerprints
- deterministic deduplication
- signal-type registry
- source-adapter interface
- adapter capability, registry and health contracts
- CI quality gates across Python 3.12–3.14

The surrounding fusion, temporal, inference, opportunity and integration packages remain reserved seams until their serial phases are implemented.

The signal-adapter boundary is intentionally narrow: adapters translate source payloads into canonical signals; they do not own crawling policy, commercial workflows, inference authority or execution.

## 9. Architectural rule

**Contracts first. Intelligence second. Integrations third. Automation last.**

This ordering protects the repository from becoming a collection of scrapers, prompts and one-off workflows whose semantics cannot be trusted or reused.
