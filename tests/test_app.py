import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Перевірка, чи завантажується HTML-сторінка"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"PNID" in response.data