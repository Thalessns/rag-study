"""Schemas for documents operations."""

from pydantic import BaseModel
from uuid import UUID

from chromadb.api.types import Metadata


class CreateDocumentRequest(BaseModel):
    """Request model for creating a document."""

    document_name: str


class DocumentResponse(BaseModel):
    """Response model for a document."""

    id: UUID
    content: str
    metadata: Metadata | None


class QueryDocumentsRequest(BaseModel):
    """Request model for querying documents."""

    querys: list[str]
    top_k: int = 3
