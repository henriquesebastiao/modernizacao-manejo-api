from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/user/',
        json={
            'email': 'test@test.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['email'] == 'test@test.com'


def test_create_user_already_exists(client, user):
    response = client.post(
        '/user/',
        json={
            'email': user.email,
            'password': user.password,
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_create_user_without_email(client):
    response = client.post(
        '/user/',
        json={
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_get_user_by_id(client, user):
    response = client.get(f'/user/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['email'] == user.email


def test_get_user_by_id_does_not_exist(client):
    response = client.get('/user/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User does not exist'}


def test_get_all_users_empty_list(client):
    response = client.get('/user/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_update_user(client, user):
    response = client.patch(
        f'/user/{user.id}',
        json={'email': 'update@email.com'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['email'] == 'update@email.com'


def test_update_user_not_exist(client):
    response = client.patch(
        '/user/1',
        json={'email': 'update@email.com'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User does not exist'}


def test_update_user_email_already_exists(client, user, other_user):
    response = client.patch(
        f'/user/{user.id}',
        json={'email': other_user.email},
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_delete_user(client, user):
    response = client.delete(f'/user/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_exist(client):
    response = client.delete('/user/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User does not exist'}
