# langgraph-mini — Agentic AI Workflows and Applications Using LangGraph

A lightweight, production-ready template repository for building **agentic AI workflows** with **LangGraph** and **LangChain**.

This repo is designed for two parallel tracks:

1. **Notebooks-first exploration (`notebooks/`)**  
   Rapidly prototype workflows (RAG, tools, persistence, HITL, multi-agent patterns) and share reproducible demos for users.

2. **Library-grade implementation (`src/`)**  
   Gradually migrate stable workflows into a structured Python package (`langgraph_mini`) with tests and CI, ready to publish to **PyPI**.

---

## Repository layout

- `notebooks/` — experimentation and tutorial notebooks (kept in the repo for learning and demos)
- `src/langgraph_mini/` — the installable Python package (production code lives here)
- `tests/` — pytest suite (includes a smoke test so CI stays green early)
- `.github/workflows/ci.yml` — CI: lint, format, tests, build, metadata checks
- `uv.lock` — reproducible dependency lock file

---

## Quickstart (local development with `uv`)

### 1) Create a virtual environment and install dependencies
```bash
# From the repo root
uv venv --python 3.11
source .venv/bin/activate

# Install dependencies (dev group) + install project (editable by default)
uv sync --dev

# Add dependencies (writes to pyproject.toml)
uv add langgraph
uv add langchain
uv add langchain_openai
uv add dotenv
uv add pydantic python-dotenv rich
uv add --dev pytest ruff mypy build twine

# Install everything (including dev deps)
uv sync

# Editable install
uv pip install -e .
````

### 2) Run the CLI (stub for now)

```bash
uv run langgraph-mini
```

### 3) Run lint, format check, tests, and build

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest -q
uv build
```

---

## Working with notebooks

Notebooks are used for rapid iteration and validation of workflows before moving them into `src/`.

Recommended workflow:

1. Build the workflow in `notebooks/`
2. Once stable, refactor into `src/langgraph_mini/...`
3. Add tests in `tests/`
4. Merge via PR (see branching model below)

> Tip: Keep notebook outputs minimal to avoid noisy diffs.

---

## Trunk-based development (TBD)

This repo follows **trunk-based development**:

* `main` should always be **green** (CI passing).
* All changes are made via **short-lived branches** and merged quickly.
* Typical flow: branch → small commits → PR → CI passes → squash merge → delete branch.

Suggested branch naming:

* `feat/...` new features
* `fix/...` bug fixes
* `docs/...` documentation
* `chore/...` maintenance

Example:

```bash
git checkout main
git pull
git checkout -b feat/add-first-langgraph-workflow
# make changes
git commit -am "feat: add first langgraph workflow notebook"
git push -u origin feat/add-first-langgraph-workflow
# open PR -> CI -> merge
```

---

## Publishing to PyPI

When the package API stabilizes:

* Ensure `src/` contains the intended public modules
* Keep `uv.lock` updated
* Add a release workflow (tag-based)
* Build and publish with `uv build` + `twine`

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

