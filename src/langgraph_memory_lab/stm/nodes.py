"""stm.nodes

LangGraph node functions for STM patterns.

Port notebook logic into these stubs:
- chat (call_model)
- trimming
- deletion (RemoveMessage)
- summarization (summary + keep last N)
"""

from __future__ import annotations

from typing import Any, Dict


def call_model(state: Any) -> Dict[str, Any]:
    """Main chat node. Return updates like {'messages': [ai_message]}."""
    raise NotImplementedError("Port your base chat node implementation here.")


def trim_context(state: Any, *, token_budget: int) -> Dict[str, Any]:
    """Trim messages to fit within a token budget."""
    raise NotImplementedError("Port trimming logic from 3_stm_trimming.ipynb.")


def delete_old_messages(state: Any, *, max_messages: int) -> Dict[str, Any]:
    """Delete old messages if message count exceeds max_messages."""
    raise NotImplementedError("Port deletion logic from 4_stm_deletion.ipynb.")


def summarize_history(state: Any) -> Dict[str, Any]:
    """Summarize older messages and keep only the most recent turns."""
    raise NotImplementedError("Port summarization logic from 5_stm_summarization.ipynb.")
