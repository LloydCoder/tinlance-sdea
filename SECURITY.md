# Security Policy

## Supported versions

| Version | Security support |
|---|---|
| `main` | Supported |
| `0.1.x` | Supported while the project remains pre-1.0 |

## Reporting a vulnerability

**Do not open a public GitHub issue for a suspected vulnerability.**

Send a private report to **hello@tinlance.com** with the subject `SDEA Security Vulnerability`. Include the affected version or commit, affected module, vulnerability class and impact, reproduction steps or proof of concept, and a proposed mitigation if known.

If GitHub private vulnerability reporting is enabled for this repository, that channel may be used instead.

## Response expectations

- Acknowledgement target: within 2 business days.
- Initial triage/update target: within 7 calendar days.
- Remediation timing depends on severity, exploitability and affected deployment surface.
- Reporter attribution will be discussed before public disclosure.

## Disclosure

Please allow the maintainers reasonable time to investigate and remediate a confirmed issue before public disclosure.

Do not include live credentials, private keys, access tokens, customer data or other sensitive material in reports.

## Security boundaries

SDEA is an intelligence substrate, not an authorization boundary. Identity, authorization, approvals, execution budgets, sandboxing and governed tool access remain external responsibilities, with Tinlance Agent Platform authoritative where integrated.
