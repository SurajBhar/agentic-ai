"""ltm.nodes

LangGraph node functions for Long-Term Memory workflows.

Port logic from:
- 7_ltm_implementation.ipynb (remember -> chat)
- 8_ltm_postgres.ipynb (persistent store)
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

from ..common.text import bullet_join
from .prompts import SYSTEM_PROMPT_TEMPLATE, MEMORY_PROMPT  # noqa: F401


def format_memories_for_prompt(memory_texts: Iterable[str]) -> str:
    """Format memory strings for the system prompt."""
    return bullet_join(memory_texts)


def read_user_memories(
    *, store: Any, user_id: str, namespace: Optional[tuple] = None, limit: int = 50
) -> List[str]:
    """Read user memories from the store (search/get)."""
    raise NotImplementedError("Implement Store read/search logic here.")


def remember_node(state: Any, *, store: Any) -> Dict[str, Any]:
    """Extract new memories from latest user message and write to store."""
    raise NotImplementedError("Port memory extraction + store writes here.")


def chat_node(state: Any, *, store: Any) -> Dict[str, Any]:
    """Chat node that reads LTM and injects into the system prompt."""
    raise NotImplementedError("Port personalized chat logic here.")
