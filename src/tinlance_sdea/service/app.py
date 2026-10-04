"""FastAPI transport and operational health surface for SDEA."""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import Any

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis import Redis

from tinlance_sdea.service.config import Settings

settings = Settings.from_env()
logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
logger = logging.getLogger("tinlance_sdea")

app = FastAPI(
    title="Tinlance SDEA",
    version=settings.version,
    description="Signal-Driven Engineering Acquisition intelligence service.",
)


def _check_database() -> tuple[bool, str]:
    if not settings.database_url:
        return False, "not_configured"
    try:
        with (
            psycopg.connect(settings.database_url, connect_timeout=3) as connection,
            connection.cursor() as cursor,
        ):
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return True, "ok"
    except Exception:
        logger.exception("database readiness check failed")
        return False, "unavailable"


def _check_redis() -> tuple[bool, str]:
    if not settings.redis_url:
        return False, "not_configured"
    try:
        client = Redis.from_url(
            settings.redis_url,
            socket_connect_timeout=3,
            socket_timeout=3,
        )
        client.ping()
        return True, "ok"
    except Exception:
        logger.exception("redis readiness check failed")
        return False, "unavailable"


@app.get("/healthz", include_in_schema=False)
def healthz() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}


@app.get("/readyz", include_in_schema=False)
def readyz() -> JSONResponse:
    database_ok, database_state = _check_database()
    redis_ok, redis_state = _check_redis()
    ready = database_ok and redis_ok
    payload: dict[str, Any] = {
        "status": "ready" if ready else "not_ready",
        "service": settings.app_name,
        "environment": settings.environment,
        "dependencies": {"database": database_state, "redis": redis_state},
    }
    return JSONResponse(status_code=200 if ready else 503, content=payload)


@app.get("/version", include_in_schema=False)
def version() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "version": settings.version,
        "environment": settings.environment,
    }


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "status": "operational",
        "health": "/healthz",
        "readiness": "/readyz",
        "version": settings.version,
        "environment": settings.environment,
        "timestamp": datetime.now(UTC).isoformat(),
    }
