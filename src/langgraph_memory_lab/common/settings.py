"""common.settings

Centralized configuration for the project.

Prefer environment variables for secrets (e.g., OPENAI_API_KEY).
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Project settings loaded from environment variables."""

    # Postgres connection string used by PostgresSaver / PostgresStore
    db_uri: str = os.getenv("DB_URI", "postgresql://postgres:postgres@localhost:5442/langgraph")

    # Model names (adjust to your provider)
    chat_model: str = os.getenv("CHAT_MODEL", "gpt-4o-mini")
    memory_model: str = os.getenv("MEMORY_MODEL", "gpt-4o-mini")

    # STM policy defaults
    token_budget: int = int(os.getenv("TOKEN_BUDGET", "4096"))
    keep_last_messages: int = int(os.getenv("KEEP_LAST_MESSAGES", "2"))
    summarize_after: int = int(os.getenv("SUMMARIZE_AFTER", "6"))


def get_settings() -> Settings:
    """Return loaded settings."""
    return Settings()
