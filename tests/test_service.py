from types import SimpleNamespace

from fastapi.testclient import TestClient

from tinlance_sdea.service import app as service_module
from tinlance_sdea.service.config import Settings


def test_healthz_is_dependency_free() -> None:
    response = TestClient(service_module.app).get("/healthz")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_version_surface_is_stable(monkeypatch) -> None:
    monkeypatch.setenv("SDEA_VERSION", "test-version")

    settings = Settings.from_env()

    assert settings.version == "test-version"


def test_readiness_fails_closed_without_dependencies(monkeypatch) -> None:
    monkeypatch.setattr(service_module, "settings", Settings(database_url="", redis_url=""))

    response = TestClient(service_module.app).get("/readyz")

    assert response.status_code == 503
    assert response.json()["status"] == "not_ready"
    assert response.json()["dependencies"] == {
        "database": "not_configured",
        "redis": "not_configured",
    }


def test_root_contains_operational_metadata(monkeypatch) -> None:
    monkeypatch.setattr(
        service_module,
        "settings",
        Settings(app_name="test-sdea", version="9.9.9", environment="test"),
    )

    response = TestClient(service_module.app).get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "test-sdea"
    assert response.json()["version"] == "9.9.9"
    assert response.json()["environment"] == "test"


def test_database_check_success(monkeypatch) -> None:
    class Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def execute(self, _query):
            return None

        def fetchone(self):
            return (1,)

    class Connection:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def cursor(self):
            return Cursor()

    class Psycopg:
        @staticmethod
        def connect(_url, connect_timeout):
            assert connect_timeout == 3
            return Connection()

    monkeypatch.setattr(service_module, "settings", Settings(database_url="postgresql://test"))
    monkeypatch.setitem(__import__("sys").modules, "psycopg", Psycopg())

    assert service_module._check_database() == (True, "ok")


def test_database_check_failure(monkeypatch) -> None:
    class Psycopg:
        @staticmethod
        def connect(_url, connect_timeout):
            raise RuntimeError("database unavailable")

    monkeypatch.setattr(service_module, "settings", Settings(database_url="postgresql://test"))
    monkeypatch.setitem(__import__("sys").modules, "psycopg", Psycopg())

    assert service_module._check_database() == (False, "unavailable")


def test_redis_check_success(monkeypatch) -> None:
    class Client:
        def ping(self):
            return True

    class Redis:
        @staticmethod
        def from_url(_url, socket_connect_timeout, socket_timeout):
            assert socket_connect_timeout == 3
            assert socket_timeout == 3
            return Client()

    monkeypatch.setattr(service_module, "settings", Settings(redis_url="redis://test"))
    monkeypatch.setitem(__import__("sys").modules, "redis", SimpleNamespace(Redis=Redis))

    assert service_module._check_redis() == (True, "ok")


def test_redis_check_failure(monkeypatch) -> None:
    class Redis:
        @staticmethod
        def from_url(_url, socket_connect_timeout, socket_timeout):
            raise RuntimeError("redis unavailable")

    class RedisModule:
        Redis = Redis

    monkeypatch.setattr(service_module, "settings", Settings(redis_url="redis://test"))
    monkeypatch.setitem(__import__("sys").modules, "redis", RedisModule())

    assert service_module._check_redis() == (False, "unavailable")
