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

    class RedisModule:
        @staticmethod
        def from_url(_url, decode_responses):
            assert decode_responses is True
            return Client()

    monkeypatch.setattr(worker, "redis", RedisModule())
    worker._STOP = False
    worker.main()
    assert worker._STOP is True
