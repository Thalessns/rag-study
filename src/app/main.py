"""Main application module."""

from fastapi import FastAPI

app = FastAPI(
    title="RAG Study",
    description="RAG Study",
    version="0.0.1"
)


@app.get("/")
def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns a dictionary with the status of the application.
    """
    return {"success": "Application is alive and well."}
