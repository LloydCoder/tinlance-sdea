"""Fail-closed Redis queue consumer for SDEA background workloads."""

from __future__ import annotations

import json
import logging
import os
import signal
from typing import Any

from redis import Redis

logging.basicConfig(level=os.getenv("SDEA_LOG_LEVEL", "INFO"))
logger = logging.getLogger("tinlance_sdea.worker")

QUEUE = os.getenv("SDEA_QUEUE_NAME", "sdea:jobs")
REDIS_URL = os.environ["REDIS_URL"]
_STOP = False


def _stop(_signum: int, _frame: Any) -> None:
    global _STOP
    _STOP = True


def _dispatch(payload: dict[str, Any]) -> None:
    job_type = payload.get("type")
    if not isinstance(job_type, str) or not job_type:
        raise ValueError("job envelope requires a non-empty string 'type'")
    raise ValueError(f"unsupported job type: {job_type}")


def main() -> None:
    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)
    client = Redis.from_url(REDIS_URL, decode_responses=True)
    logger.info("SDEA worker started; queue=%s", QUEUE)

    while not _STOP:
        item = client.brpop(QUEUE, timeout=5)
        if item is None:
            continue
        _, raw_payload = item
        try:
            payload = json.loads(raw_payload)
            if not isinstance(payload, dict):
                raise ValueError("job payload must be a JSON object")
            _dispatch(payload)
        except Exception:
            logger.exception("job rejected; payload was not executed")

    client.close()
    logger.info("SDEA worker stopped")


if __name__ == "__main__":
    main()
