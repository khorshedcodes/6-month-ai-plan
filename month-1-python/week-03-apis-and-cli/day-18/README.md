# Day 18: Professional Python Packaging, `src/` Layout & Linting with Ruff

## Learning Objectives
1. Flat vs. `src/` project layout in enterprise Python applications.
2. The role of `__init__.py`: package namespaces and public API exposure (`__all__`).
3. Absolute vs. Relative imports (and solving the classic `ImportError: attempted relative import with no known parent package`).
4. Modern Python tooling: Linting and formatting at lightning speed with `ruff` (replacing flake8, black, isort).
5. Writing a `pyproject.toml` file to configure linter rules.

---

## Daily Task: Package a Clean CLI Package (Without AI)
Structure a multi-module package:
```text
day-18/
├── pyproject.toml
└── src/
    └── logpulse/
        ├── __init__.py
        ├── core.py      # Core parser / business logic
        ├── utils.py     # Timestamp and file helpers
        └── cli.py       # argparse entry point
```
1. Implement modules with absolute/relative imports.
2. Expose high-level functions cleanly in `__init__.py`.
3. Run `ruff check .` to catch code smells, unused imports, and style bugs.
4. Run `ruff format .` to format the code to industry standards.

---

## Developer English Task: Code Review & Style Guides
Explain in 3-4 professional C1-level sentences:
*"Why is the `src/` layout preferred over putting source files directly in the root directory of a Python repository?"*
