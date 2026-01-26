"""stm.policies

STM policies define how chat history is managed to stay within context windows.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrimPolicy:
    """Config for trimming messages to a token budget."""
    token_budget: int


@dataclass(frozen=True)
class DeletionPolicy:
    """Config for deleting old messages after a threshold."""
    max_messages: int


@dataclass(frozen=True)
class SummarizationPolicy:
    """Config for summarization trigger and retention."""
    summarize_after: int
    keep_last_messages: int


def should_summarize(*, message_count: int, policy: SummarizationPolicy) -> bool:
    """True if summarization should run given the policy."""
    return message_count >= policy.summarize_after
