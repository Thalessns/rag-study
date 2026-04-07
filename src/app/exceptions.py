"""Custom exceptions for the application."""

from fastapi import HTTPException, status


class CustomBaseException(HTTPException):
    """Base class for custom exceptions."""

    STATUS_CODE = status.HTTP_418_IM_A_TEAPOT
    DETAIL = "An error occurred and i am a teapot btw."
