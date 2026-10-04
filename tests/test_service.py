from fastapi.testclient import TestClient

from tinlance_sdea.service.app import app


def test_healthz_is_dependency_free() -> None:
    response = TestClient(app).get("/healthz")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_version_surface_is_stable(monkeypatch) -> None:
    monkeypatch.setenv("SDEA_VERSION", "test-version")
    from tinlance_sdea.service.config import Settings

    settings = Settings.from_env()

    assert settings.version == "test-version"


def test_readiness_fails_closed_without_dependencies() -> None:
    from tinlance_sdea.service import app as service_module

    original_database = service_module.settings.database_url
    original_redis = service_module.settings.redis_url
    service_module.settings.database_url = ""
    service_module.settings.redis_url = ""
    try:
        response = TestClient(service_module.app).get("/readyz")
        assert response.status_code == 503
        assert response.json()["status"] == "not_ready"
        assert response.json()["dependencies"] == {
            "database": "not_configured",
            "redis": "not_configured",
        }
    finally:
        service_module.settings.database_url = original_database
        service_module.settings.redis_url = original_redis
