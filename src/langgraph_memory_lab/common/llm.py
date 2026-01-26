"""common.llm

Factory helpers for creating LLM clients.

Wire these to your actual provider (e.g., ChatOpenAI) once dependencies are added.
Keeping factories here makes it easier to swap models and test.
"""

from __future__ import annotations

from typing import Any, Optional

from .settings import get_settings


def make_chat_llm(*, temperature: float = 0.0, model: Optional[str] = None, **kwargs: Any):
    """Create the LLM used for normal chat responses."""
    settings = get_settings()
    model_name = model or settings.chat_model
    raise NotImplementedError(
        "Implement chat LLM factory (e.g., langchain_openai.ChatOpenAI). "
        f"Requested model={model_name}"
    )


def make_memory_llm(*, temperature: float = 0.0, model: Optional[str] = None, **kwargs: Any):
    """Create the LLM used for memory extraction/deduplication."""
    settings = get_settings()
    model_name = model or settings.memory_model
    raise NotImplementedError(
        f"Implement memory LLM factory (often same provider/model). Requested model={model_name}"
    )
