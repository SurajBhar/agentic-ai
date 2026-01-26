"""stm.graphs

Graph builder functions for STM workflows.

These should return compiled graphs.
"""

from __future__ import annotations

from typing import Any, Optional

from ..common.settings import get_settings
from .policies import TrimPolicy, DeletionPolicy, SummarizationPolicy
from .checkpointers import postgres_checkpointer


def build_basic_stm_graph(*, checkpointer: Optional[Any] = None) -> Any:
    """Basic single-node STM chat graph (notebook: 1_stm.ipynb)."""
    raise NotImplementedError("Compile a StateGraph(MessagesState) with call_model node.")


def build_postgres_stm_graph(*, db_uri: Optional[str] = None) -> Any:
    """Basic STM graph with Postgres checkpointing (notebook: 2_stm_persistence.ipynb)."""
    cp = postgres_checkpointer(db_uri)
    return build_basic_stm_graph(checkpointer=cp)


def build_trimming_stm_graph(*, policy: Optional[TrimPolicy] = None, checkpointer: Optional[Any] = None) -> Any:
    """STM graph with trimming policy (notebook: 3_stm_trimming.ipynb)."""
    settings = get_settings()
    policy = policy or TrimPolicy(token_budget=settings.token_budget)
    raise NotImplementedError("Compile trim -> call_model workflow.")


def build_deletion_stm_graph(*, policy: Optional[DeletionPolicy] = None, checkpointer: Optional[Any] = None) -> Any:
    """STM graph with deletion policy (notebook: 4_stm_deletion.ipynb)."""
    raise NotImplementedError("Compile call_model -> delete_old_messages workflow.")


def build_summarization_stm_graph(*, policy: Optional[SummarizationPolicy] = None, checkpointer: Optional[Any] = None) -> Any:
    """STM graph with summarization (notebook: 5_stm_summarization.ipynb)."""
    settings = get_settings()
    policy = policy or SummarizationPolicy(
        summarize_after=settings.summarize_after,
        keep_last_messages=settings.keep_last_messages,
    )
    raise NotImplementedError("Compile conditional summarize -> chat flow.")
