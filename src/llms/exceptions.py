"""Custom exceptions for the LLMs module."""

from fastapi import status

from src.app.exceptions import CustomBaseException


class GeminiAPIErrorException(CustomBaseException):
    """Exception raised when there is an error with the Gemini API."""

    DETAIL = "An error occurred while communicating with the Gemini API. Error details: {details}"

    def __init__(self, status_code: int, details: str) -> None:
        super().__init__(status_code=status_code, detail=self.DETAIL.format(details=details))
