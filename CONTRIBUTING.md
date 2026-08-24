# Contributing

Thanks for your interest in improving the NYC 311 Service Operations Analytics project.

## Development Workflow

1. Create a branch from `main`.
2. Keep changes focused on one analytical or engineering improvement.
3. Run the local checks before opening a pull request:

```bash
make test
```

4. Use clear commit messages that describe the change.
5. Open a pull request with a short summary, testing notes, and any analytical assumptions introduced.

## Contribution Areas

Useful contributions include:

- improving data-quality checks,
- adding or refining SQL analysis,
- extending automated tests,
- improving dashboard documentation,
- documenting analytical assumptions and caveats,
- improving pipeline reliability or reproducibility.

## Data and Reproducibility

Do not commit the full NYC 311 source dataset. Use the repository's API-based extraction workflow instead so analyses remain reproducible.

When changing transformations or KPI definitions, document the rationale and update related tests or documentation where appropriate.

## Pull Request Checklist

- [ ] The change has a clear purpose.
- [ ] Existing tests pass.
- [ ] New logic is tested when appropriate.
- [ ] Documentation is updated if behavior or analytical definitions changed.
- [ ] No large generated datasets or credentials are committed.
