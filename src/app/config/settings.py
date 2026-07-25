from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    # Application
    app_name: str = "AI Personal Communication Assistant"
    app_env: str = "development"
    debug: bool = True

    # Database
    database_path: str = "./data/database"
    database_name: str = "assistant.duckdb"

    # Logging
    log_level: str = "INFO"
    log_retention_days: int = 30
    log_rotation: str = "10 MB"
    log_json: bool = False
    log_path: str = "./logs"

    # Scheduler
    sync_interval_minutes: int = 30

    # AI
    llm_enabled: bool = False
    llm_model: str = ""
    llm_memory_limit_mb: int = 2048

    # Connectors
    gmail_enabled: bool = False
    outlook_enabled: bool = False

    # Analytics
    enable_analytics: bool = True

    # Voice
    voice_enabled: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )


settings = Settings()
