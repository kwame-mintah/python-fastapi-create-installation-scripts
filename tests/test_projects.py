from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_project_details():
    response = client.get("/projects/bxsHg/details")
    assert response.status_code == 200
    assert response.json() == {
        "details": {
            "softwarePackages": [
                {"name": "openjdk", "version": "13"},
                {"name": "node", "version": "18.16.1"},
                {"name": "python", "version": "3.9"},
            ]
        },
        "projectId": "bxsHg",
        "projectName": "Cartoon Network",
    }


def test_get_project_details_invalid():
    response = client.get("/projects/invalid/details")
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}
