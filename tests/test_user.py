from http import HTTPStatus


def test_read_users(client):
    response = client.get('/user/')

    assert response.json() == []
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/user/',
        json={
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['email'] == 'alice@example.com'
