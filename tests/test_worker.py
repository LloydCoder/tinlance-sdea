from types import SimpleNamespace

import importlib
import sys


def _worker_module(monkeypatch):
    monkeypatch.setenv("REDIS_URL", "redis://test")
    sys.modules.pop("tinlance_sdea.service.worker", None)
    return importlib.import_module("tinlance_sdea.service.worker")


def test_dispatch_rejects_missing_type(monkeypatch) -> None:
    worker = _worker_module(monkeypatch)

    try:
        worker._dispatch({})
    except ValueError as exc:
        assert "type" in str(exc)
    else:
        raise AssertionError("missing job type must be rejected")


def test_dispatch_rejects_unknown_type(monkeypatch) -> None:
    worker = _worker_module(monkeypatch)

    try:
        worker._dispatch({"type": "unknown"})
    except ValueError as exc:
        assert "unsupported job type" in str(exc)
    else:
        raise AssertionError("unknown job type must be rejected")


def test_worker_stops_cleanly(monkeypatch) -> None:
    worker = _worker_module(monkeypatch)

    class Client:
        def brpop(self, _queue, timeout):
            assert timeout == 5
            worker._STOP = True
            return None

        def close(self):
            return None

    monkeypatch.setattr(
        worker,
        "redis",
        SimpleNamespace(
            Redis=SimpleNamespace(
                from_url=lambda _url, decode_responses: Client(),
            )
        ),
    )
    worker._STOP = False
    worker.main()
    assert worker._STOP is True


def test_worker_rejects_malformed_payload(monkeypatch) -> None:
    worker = _worker_module(monkeypatch)

    class Client:
        def __init__(self):
            self.calls = 0

        def brpop(self, _queue, timeout):
            assert timeout == 5
            self.calls += 1
            if self.calls == 1:
                return ("sdea:jobs", "{not-json")
            worker._STOP = True
            return None

        def close(self):
            return None

    monkeypatch.setattr(
        worker,
        "redis",
        SimpleNamespace(
            Redis=SimpleNamespace(
                from_url=lambda _url, decode_responses: Client(),
            )
        ),
    )
    worker._STOP = False
    worker.main()
    assert worker._STOP is True
