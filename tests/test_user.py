from http import HTTPStatus


def test_read_users(client):
    response = client.get('/user/')

    assert response.json() == []
    assert response.status_code == HTTPStatus.OK
