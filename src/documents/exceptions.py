"""Custom exceptions for the documents module."""

from fastapi import status

from src.app.exceptions import CustomBaseException


class DocumentNameNotFoundException(CustomBaseException):
    """Exception raised when a document name is not found."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Document with name '{document_name}' was not found."


class DocumentIDNotFoundException(CustomBaseException):
    """Exception raised when a document ID is not found."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Document with ID '{document_id}' was not found."
