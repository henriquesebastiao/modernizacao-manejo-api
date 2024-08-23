from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


def test_create_user_deve_retornar_201():
    client = TestClient(app)

    response = client.post(
        '/user/',
        json={
            'first_name': 'Test',
            'last_name': 'Pytest',
            'email': 'test@pytest.com',
            'password': 'segura123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    # Criar assert com JSON
