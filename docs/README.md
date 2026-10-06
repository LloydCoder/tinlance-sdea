# SDEA Documentation

Use this page as the documentation map.

| Type | Location | Purpose |
|---|---|---|
| Tutorial / first run | [README Quick Start](../README.md#quick-start) | Install and verify the package |
| How-to | [Deployment runbook](../deploy/README.md) | Deploy the first-stage VPS profile |
| Explanation | [Architecture](architecture.md) | Understand system boundaries and data flow |
| Explanation | [Domain model](domain-model.md) | Understand canonical semantic contracts |
| Reference | [Roadmap](roadmap.md) | Delivery status and definition of done |
| Reference | [ADRs](adr/README.md) | Architectural decisions and permanent boundaries |

## Documentation rule

Code is the source of truth for implemented fields and behavior. Documentation describes semantics, boundaries and supported workflows. When implementation changes a contract, update the relevant reference and tests in the same pull request.

Prefer repository-relative links for internal documentation. Use external links only for authoritative standards, dependencies and supporting references.
