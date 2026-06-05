"""Ponto de entrada da API FastAPI. Rotas de negócio sob `/api/v1/`."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.meetings import router as meetings_router
from app.config import get_settings
from app.db import init_db


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    settings.upload_dir.mkdir(parents=True, exist_ok=True)
    init_db()
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
    app.include_router(meetings_router, prefix=settings.api_v1_prefix)

    @app.get("/health", tags=["infra"], summary="Healthcheck")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
