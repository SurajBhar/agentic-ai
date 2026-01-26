# src/INFO.md — What’s inside `src/`

This repository uses a **src-layout**. The Python package lives under:

- `src/langgraph_memory_lab/`

The goal of this codebase is to provide **clean, reusable modules** derived from tutorial notebooks:
Short-Term Memory (STM) patterns using LangGraph checkpoints, and Long-Term Memory (LTM) patterns using LangGraph Store.

---

## Package overview

### `langgraph_memory_lab/common/`
Shared utilities used by both STM and LTM modules.

- `settings.py` — defaults like model names, DB URI, token budgets
- `llm.py` — LLM factory helpers
- `text.py` — small formatting helpers

---

## STM: Short-Term Memory (checkpoints + message history)

### `langgraph_memory_lab/stm/`
- `checkpointers.py` — InMemorySaver / PostgresSaver helpers
- `policies.py` — trimming/deletion/summarization policies
- `nodes.py` — node functions (chat, trim, delete, summarize)
- `graphs.py` — graph builders (basic/persist/trim/delete/summarize)

---

## LTM: Long-Term Memory (Store API + extraction + personalization)

### `langgraph_memory_lab/ltm/`
- `schemas.py` — Pydantic models for memory extraction
- `prompts.py` — prompt templates (system + memory extraction)
- `stores.py` — InMemoryStore / PostgresStore helpers
- `nodes.py` — remember/chat node functions
- `graphs.py` — graph builders (chat-only, remember->chat)
- `embedding_demo.py` — optional semantic search demo

---

## Notes
- Add dependencies in your repo’s `pyproject.toml` / requirements once you wire implementations.
- Postgres-backed modules assume a running Postgres instance + valid `DB_URI`.
- LTM typically uses `config["configurable"]["user_id"]` to isolate per-user memory.
