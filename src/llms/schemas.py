"""Schemas for LLMs operations."""

from pydantic import BaseModel


class LLMInfo(BaseModel):
    """Model info response schema."""

    name: str
    supported_actions: list[str]
    

class CompletionRequest(BaseModel):
    """Completion request schema."""

    model: str
    content: str


class CompletionUsage(BaseModel):
    """Completion usage schema."""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class CompletionResponse(BaseModel):
    """Completion response schema."""

    contents: list[str]
    usage: CompletionUsage
