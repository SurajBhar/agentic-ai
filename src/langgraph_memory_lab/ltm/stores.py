"""ltm.stores

Helpers to configure long-term memory stores.

Notebook mapping:
- 6_ltm_basics.ipynb (InMemoryStore)
- 8_ltm_postgres.ipynb (PostgresStore)
"""

from __future__ import annotations

from typing import Optional, Any

from ..common.settings import get_settings


def inmemory_store() -> Any:
    """Return an InMemoryStore."""
    raise NotImplementedError("Implement InMemoryStore factory here.")


def postgres_store(db_uri: Optional[str] = None) -> Any:
    """Return a PostgresStore and run setup()."""
    settings = get_settings()
    uri = db_uri or settings.db_uri
    raise NotImplementedError(f"Implement PostgresStore factory here for DB_URI={uri!r}.")
