"""ltm.graphs

Graph builder functions for Long-Term Memory workflows.
"""

from __future__ import annotations

from typing import Any, Optional

from .stores import postgres_store


def build_ltm_chat_graph(*, store: Optional[Any] = None) -> Any:
    """Build a read-only personalized chat graph (no memory writes)."""
    raise NotImplementedError("Compile a graph that uses ltm.nodes.chat_node with a store.")


def build_remember_then_chat_graph(*, store: Optional[Any] = None) -> Any:
    """Build a graph: remember -> chat."""
    raise NotImplementedError("Compile a graph chaining remember_node then chat_node.")


def build_postgres_remember_then_chat_graph(*, db_uri: Optional[str] = None) -> Any:
    """Build remember->chat graph backed by PostgresStore."""
    store = postgres_store(db_uri)
    return build_remember_then_chat_graph(store=store)
