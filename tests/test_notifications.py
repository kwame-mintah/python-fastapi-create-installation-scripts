from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_notifications():
    response = client.get("/notifications")
    assert response.status_code == 200
    assert response.json() == {
        "notifications": [
            {"message": "Just smile", "notificationId": 1},
            {"message": "And wave", "notificationId": 2},
        ]
    }
