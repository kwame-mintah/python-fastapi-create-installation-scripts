from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the users endpoint"}


def test_get_user_details():
    response = client.get("/user/0x00/details")
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "Jonny",
        "lastName": "Test",
        "location": "London",
        "role": "Software Engineer",
    }
