import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.mark.test_endpoints
def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'Ollivanders shop' in response.data
