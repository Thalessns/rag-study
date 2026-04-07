"""Settings for the application."""

from pydantic import BaseSettings

class AppSettings(BaseSettings):
    """Application settings."""

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_RELOAD: bool = False
    APP_LOG_LEVEL: str = "INFO"


app_settings = AppSettings()
