"""stm.checkpointers

Helpers for configuring LangGraph checkpointing (Short-Term Memory persistence).

- InMemorySaver: good for tutorials/tests
- PostgresSaver: persistence across processes and restarts
"""

from __future__ import annotations

from typing import Optional

from ..common.settings import get_settings


def inmemory_checkpointer():
    """Return an in-memory checkpointer (InMemorySaver)."""
    raise NotImplementedError("Implement InMemorySaver factory here.")


def postgres_checkpointer(db_uri: Optional[str] = None):
    """Return a Postgres-backed checkpointer (PostgresSaver) and run setup()."""
    settings = get_settings()
    uri = db_uri or settings.db_uri
    raise NotImplementedError(f"Implement PostgresSaver factory here for DB_URI={uri!r}.")
