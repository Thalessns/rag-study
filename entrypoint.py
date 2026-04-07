"""Entrypoint for the application."""

import uvicorn

from src.app.settings import app_settings


if __name__ == "__main__":
    uvicorn.run(
        "src.app.main:app",
        host=app_settings.APP_HOST,
        port=app_settings.APP_PORT,
        reload=app_settings.APP_RELOAD
    )
