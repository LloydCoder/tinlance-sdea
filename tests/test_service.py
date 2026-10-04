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
