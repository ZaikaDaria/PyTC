import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_homepage(client):
    assert client.get('/').status_code == 200


def test_greet(client):
    response = client.post("/", data={"name": "Daria"})
    assert response.status_code == 200
