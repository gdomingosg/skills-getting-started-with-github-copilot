import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_register_participant():
    activity_name = "Yoga Class"
    email = "test@example.com"
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 200
    assert "message" in response.json()


def test_unregister_participant():
    activity_name = "Yoga Class"
    email = "test@example.com"
    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert response.status_code == 200 or response.status_code == 404