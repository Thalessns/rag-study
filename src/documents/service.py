"""Module for documents service."""

import os

from chromadb import PersistentClient
from chromadb.api.models.Collection import Collection
from chromadb.api.types import GetResult, QueryResult
from uuid import UUID, uuid4

from src.documents.exceptions import (
    DocumentIDNotFoundException,
    DocumentNameNotFoundException,
)
from src.documents.schemas import DocumentResponse


class DocumentsService:
    """Service for managing documents."""

    __client: PersistentClient
    __collection: Collection

    def __init__(self) -> None:
        """Initialize the service."""

        self.__client = PersistentClient(path="./chroma_db")
        self.__collection = self.__client.get_or_create_collection(name="documents")

    async def add_document(self, document_name: str) -> DocumentResponse:
        """Add a document to the collection.

        Args:
            document_name (str): The name of the document to add the content.

        Returns:
            DocumentResponse: The added document and its metadata.
        """
        content = await self.__read_document(document_name)
        document_id = uuid4()
        self.__collection.add(documents=[content], ids=[str(document_id)])
        return await self.get_document(document_id)

    async def get_document(self, document_id: UUID) -> DocumentResponse:
        """Get a document from the collection.

        Args:
            document_id (UUID): The ID of the document to get.

        Returns:
            DocumentResponse: The document and its metadata.
        """
        documents = self.__collection.get(ids=[str(document_id)])
        if not documents["documents"]:
            raise DocumentIDNotFoundException(document_id=document_id)
        document = await self.__to_document_response(documents)
        return document[0]

    async def list_documents(self) -> list[DocumentResponse]:
        """List all documents in the collection.

        Returns:
            list[DocumentResponse]: A list of documents and their metadata.
        """
        documents = self.__collection.get()
        return await self.__to_document_response(documents)

    async def query_documents(self, querys: list[str], top_k: int) -> QueryResult:
        """Query the collection for similar documents.

        Args:
            querys (list[str]): The query to search for.
            top_k (int): The number of similar documents to return.

        Returns:
            list[]: The similar documents and their metadata.
        """
        return self.__collection.query(query_texts=querys, n_results=top_k)

    async def __read_document(self, document_name: str) -> list[str]:
        """Read a document from the collection.

        Args:
            document_name (str): The name of the document to read.

        Returns:
            list[str]: The content of the document.

        Raises:
            DocumentNameNotFoundException: If the document is not found.
        """
        with os.scandir("src/documents/data/") as it:
            if document_name not in [entry.name for entry in it if entry.is_file()]:
                raise DocumentNameNotFoundException(document_name=document_name)
        with open(
            f"src/documents/data/{document_name}", encoding="utf-8", mode="r"
        ) as file:
            content = file.read()
        return content

    async def __to_document_response(
        self, documents: GetResult
    ) -> list[DocumentResponse]:
        """Convert a document to a response model.

        Args:
            document (GetResult): The documents to convert.

        Returns:
            list[DocumentResponse]: The converted documents.
        """
        result = []
        for id, content, metadata in zip(
            documents["ids"], documents["documents"], documents["metadatas"]
        ):
            result.append(DocumentResponse(id=id, content=content, metadata=metadata))
        return result


documents_service = DocumentsService()
