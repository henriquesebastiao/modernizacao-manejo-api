from fastapi.testclient import TestClient

from app.main import app


def test_root_deve_retornar_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
