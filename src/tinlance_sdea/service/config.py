"""Environment-backed runtime configuration for the SDEA service."""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Settings:
    app_name: str = field(default="tinlance-sdea")
    environment: str = field(default="production")
    version: str = field(default="0.1.0")
    database_url: str = field(default="")
    redis_url: str = field(default="")
    log_level: str = field(default="INFO")

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            app_name=os.getenv("SDEA_APP_NAME", cls.app_name),
            environment=os.getenv("SDEA_ENVIRONMENT", cls.environment),
            version=os.getenv("SDEA_VERSION", cls.version),
            database_url=os.getenv("DATABASE_URL", ""),
            redis_url=os.getenv("REDIS_URL", ""),
            log_level=os.getenv("SDEA_LOG_LEVEL", cls.log_level),
        )
