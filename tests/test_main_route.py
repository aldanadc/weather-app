import pytest
from fastapi.testclient import TestClient
from weather_api.main import app


client = TestClient(app)

@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER_NAME", "TestingUser")


def test_read_main(mock_env_user):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this API's home page, TestingUser. Visit the docs here: http:/localhost:8080/weather-api-service/docs"}