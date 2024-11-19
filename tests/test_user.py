from http import HTTPStatus

from sqlalchemy import select

from app.models import User


def test_create_user(client):
    response = client.post(
        '/user/',
        json={
            'email': 'test@test.com',
            'password': 'secret',
            'first_name': 'First Name',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    response = response.json()

    assert response['first_name'] == 'First Name'
    assert response['last_name'] is None
    assert response['email'] == 'test@test.com'
    assert isinstance(response['id'], int)
    assert response['phone'] is None
    assert response['manager_id'] is None
    assert response['active']


def test_create_user_already_exists(client, user):
    response = client.post(
        '/user/',
        json={
            'email': user.email,
            'password': user.password,
            'first_name': 'Second Name',
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


def test_create_user_subordinate(client, auth, user):
    farmer = client.post(
        '/farmer/',
        headers=auth,
        json={
            'user_id': user.id,
            'farmer_plan': 'free',
        },
    )

    farm = client.post('/farm/', headers=auth, json={'name': 'Fazendinha'})

    client.post(
        '/employment/',
        headers=auth,
        json={
            'user_id': user.id,
            'farmer_id': farmer.json()['id'],
            'farm_id': farm.json()['id'],
            'employment_position': 'farmer',
        },
    )

    response = client.post(
        '/user/employee/',
        headers=auth,
        json={
            'email': 'test@test.com',
            'password': 'secret',
            'first_name': 'First Name',
            'manager_id': user.id,
        },
    )

    assert response.status_code == 201


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


def test_update_user(client, user, auth):
    response = client.patch(
        f'/user/{user.id}',
        json={'email': 'update@email.com'},
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['email'] == 'update@email.com'


def test_update_user_email_already_exists(client, user, other_user, auth):
    response = client.patch(
        f'/user/{user.id}',
        json={'email': other_user.email},
        headers=auth,
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_update_other_user_without_permission(client, user, other_user, auth):
    response = client.patch(
        f'/user/{other_user.id}',
        json={'email': 'update@email.com'},
        headers=auth,
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_update_my_user_without_permission(client, user):
    response = client.patch(
        f'/user/{user.id}',
        json={'email': 'update@email.com'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED


async def test_password_hash_in_update_user(aclient, auth, user, session):
    password = 'pwd'
    assert user.password != password
    await aclient.patch(f'/user/{user.id}', json={'password': password})
    db_user = await session.scalar(select(User).where(User.id == user.id))
    assert db_user.password != password


def test_delete_user(client, user, auth):
    response = client.delete(f'/user/{user.id}', headers=auth)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_other_user_without_permission(client, other_user, auth):
    response = client.delete(f'/user/{other_user.id}', headers=auth)

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_delete_my_user_without_permission(client, user):
    response = client.delete(f'/user/{user.id}')

    assert response.status_code == HTTPStatus.UNAUTHORIZED
