from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_dashboard_properties():
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert response.json() == {
        "assignedProjects": 2,
        "securityHotspots": {"critical": 1, "high": 1, "low": 1, "medium": 0},
        "updates": {
            "changes": "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit, sed do eiusmod tempor incididunt ut labore et "
            "dolore magna aliqua."
        },
    }
