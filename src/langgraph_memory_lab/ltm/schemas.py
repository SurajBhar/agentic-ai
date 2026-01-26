"""ltm.schemas

Pydantic models used for structured memory extraction.

Port the models from 7_ltm_implementation.ipynb into this module.
"""

from __future__ import annotations

from typing import List, Optional

try:
    from pydantic import BaseModel, Field
except Exception:  # pragma: no cover
    BaseModel = object  # type: ignore

    def Field(*args, **kwargs):  # type: ignore
        return None


class MemoryItem(BaseModel):
    """A single long-term memory item about the user."""

    content: str = Field(
        ..., description="The memory content to store (fact/preference/project detail)."
    )
    is_new: bool = Field(True, description="Whether this is new vs a duplicate.")


class MemoryDecision(BaseModel):
    """Decision about whether to write memories and which ones."""

    should_write_memory: bool = Field(
        ..., description="True if we should store at least one memory."
    )
    memories: List[MemoryItem] = Field(default_factory=list)
    reasoning: Optional[str] = Field(None, description="Optional debug reasoning (do not store).")
