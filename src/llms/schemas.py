"""Schemas for LLMs operations."""

from pydantic import BaseModel


class DocumentRetrievalConfig(BaseModel):
    """Document retrieval configuration schema."""

    querys: list[str]
    top_k: int = 3


class LLMInfo(BaseModel):
    """Model info response schema."""

    name: str
    supported_actions: list[str]


class CompletionRequest(BaseModel):
    """Completion request schema."""

    model: str
    input: str
    document_retrieval_config: DocumentRetrievalConfig | None = None


class CompletionUsage(BaseModel):
    """Completion usage schema."""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class CompletionResponse(BaseModel):
    """Completion response schema."""

    contents: str
    usage: CompletionUsage
