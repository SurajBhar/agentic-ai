"""common.text

Small string/text helper utilities used across STM/LTM modules.
"""

from __future__ import annotations

from typing import Iterable


def bullet_join(items: Iterable[str]) -> str:
    """Join strings as a bullet list."""
    items = [i.strip() for i in items if i and i.strip()]
    if not items:
        return ""
    return "\n".join(f"- {i}" for i in items)
