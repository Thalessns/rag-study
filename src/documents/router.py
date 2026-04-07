"""Router for documents endpoints."""

from fastapi import APIRouter, status

from src.documents.schemas import (
    CreateDocumentRequest,
    DocumentResponse,
    QueryDocumentsRequest,
    
)
from src.documents.service import documents_service

documents_router = APIRouter(prefix="/documents", tags=["documents"])


@documents_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_document(data: CreateDocumentRequest) -> DocumentResponse:
    """Create a new document.

    Args:
        data (CreateDocumentRequest): The request containing the document name.

    Returns:
        DocumentResponse: The created document and its metadata.
    """
    return await documents_service.add_document(document_name=data.document_name)


@documents_router.get("/", status_code=status.HTTP_200_OK)
async def list_documents() -> list[DocumentResponse]:
    """List all documents.

    Returns:
        list[DocumentResponse]: A list of documents and their metadata.
    """
    return await documents_service.list_documents()


@documents_router.get("/{document_id}", status_code=status.HTTP_200_OK)
async def get_document(document_id: str) -> DocumentResponse:
    """Get a document by its ID.

    Args:
        document_id (str): The ID of the document to get.

    Returns:
        DocumentResponse: The document and its metadata.
    """
    return await documents_service.get_document(document_id)


@documents_router.post("/query", status_code=status.HTTP_200_OK)
async def query_documents(data: QueryDocumentsRequest):
    """Query the collection for similar documents.

    Args:
        data (QueryDocumentsRequest): The query request containing the query strings and the
        number of top similar documents to return.

    Returns:
        list[]: The similar documents and their metadata.
    """
    return await documents_service.query_documents(data.querys, data.top_k)
