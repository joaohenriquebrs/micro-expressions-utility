"""Configuração da aplicação via pydantic-settings (prefixo de env `APP_`)."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações carregadas de variáveis de ambiente / arquivo `.env`."""

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")

    app_name: str = "micro-expressions-utility"
    api_v1_prefix: str = "/api/v1"

    # SQLite em dev; mesmo schema migra para PostgreSQL em prod (JSON salvo como TEXT).
    database_url: str = "sqlite:///./data/app.db"

    # Vídeos vivem no filesystem; o banco guarda só o caminho.
    upload_dir: Path = Path("data/uploads")

    # Limites de upload (questionário: 200 MB / 30 min).
    max_upload_bytes: int = 200 * 1024 * 1024
    max_duration_seconds: int = 30 * 60
    allowed_content_types: tuple[str, ...] = ("video/mp4", "video/quicktime", "video/webm")


@lru_cache
def get_settings() -> Settings:
    """Retorna as configurações em cache (instância única por processo)."""
    return Settings()
