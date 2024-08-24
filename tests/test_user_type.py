from http import HTTPStatus


def test_create_user_type(client):
    response = client.post(
        '/user/type/',
        json={'type': 'type_test'},
    )

    assert response.json() == {
        'id': 1,
        'type': 'type_test',
    }
    assert response.status_code == HTTPStatus.CREATED
