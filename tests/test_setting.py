from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_settings():
    response = client.get("/settings")
    assert response.status_code == 200
    assert response.json() == {"operatingSystem": "macOS", "version": "13.4 (22F66)"}
