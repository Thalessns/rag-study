"""Main application module."""

from fastapi import FastAPI

from src.llms.router import llms_router

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
    return {"message": "Application is alive and well."}


app.include_router(llms_router)
