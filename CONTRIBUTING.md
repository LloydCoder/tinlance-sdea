# Contributing

Thank you for contributing to Tinlance SDEA.

## Before you start

Read [README.md](README.md), [docs/architecture.md](docs/architecture.md), [docs/domain-model.md](docs/domain-model.md) and [docs/roadmap.md](docs/roadmap.md).

SDEA is an intelligence substrate. Do not introduce CRM, outreach, generic scraping, engineering execution, authorization or agent-runtime responsibilities without an approved architecture decision record.

## Development workflow

1. Fork the repository.
2. Create a focused branch from `main`.
3. Install development dependencies with `python -m pip install -e ".[dev]"`.
4. Implement the smallest coherent change.
5. Add or update tests and documentation.
6. Run the local quality gates.
7. Open a pull request using the repository template.

## Quality gates

```bash
ruff check .
ruff format --check .
mypy src
pytest --cov=tinlance_sdea --cov-report=term-missing
```

Coverage must remain at or above the repository's configured 90% threshold.

## Coding standards

- Python 3.12+.
- Prefer typed, immutable domain contracts.
- Preserve timezone-aware timestamps.
- Reject ambiguous entity matches rather than guessing.
- Keep evidence lineage explicit.
- Preserve the distinction between inference and fact.
- Avoid provider-specific semantics in canonical domain contracts.
- Keep security-sensitive behavior fail-closed.
- Update documentation when contracts or boundaries change.

## Commits

Use Conventional Commits where practical, for example `feat(domain): add capability relationship contract`, `fix(temporal): reject naive timestamps`, `docs: clarify opportunity lifecycle` and `test(evaluation): add calibration regression case`.

## Pull requests

A pull request should explain what changed, why it changed, affected contracts or boundaries, tests and validation performed, documentation changes, and security or compatibility considerations.

Keep unrelated refactors out of feature or bug-fix pull requests.

## Architecture changes

If a proposal changes SDEA's permanent ownership boundary, add or update an ADR under [docs/adr/](docs/adr/) before implementation.

## Security

Do not disclose vulnerabilities in public issues. Follow [SECURITY.md](SECURITY.md).
