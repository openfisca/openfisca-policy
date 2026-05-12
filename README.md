# OpenFisca Policy

Policy-oriented survey simulation helpers extracted from OpenFisca Survey Manager.

This package contains simulations, scenario helpers, aggregates, calibration, matching, COICOP helpers and legislation-as-of utilities. It depends on `OpenFisca-Data-Manager` for survey data access.

## Development

```shell
uv sync --extra dev
uv run pytest
uv run ruff check
```
