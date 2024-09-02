from http import HTTPStatus


def test_create_farmer(client, user, token):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    assert response.status_code == HTTPStatus.CREATED


def test_create_farmer_not_current_user(client, other_user, token):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': other_user.id, 'farmer_plan': 'starter'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_create_more_one_farmer_for_one_user(client, user, token):
    client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response.status_code == HTTPStatus.CONFLICT
    response.json() == {'detail': 'There is already a Farmer for this user'}


def test_get_farmer(client, user, token):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.get(f'/farmer/{response.json()['id']}')

    assert response.status_code == HTTPStatus.OK


def test_get_farmer_not_exist(client):
    response = client.get('/farmer/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    response.json() == {'detail': 'Farmer does not exist'}


def test_get_all_farmers(client):
    response = client.get('/farmer/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'farmers': []}


def test_update_farmer(client, token, user):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.patch(
        f'/farmer/{response.json()['id']}',
        headers={'Authorization': f'Bearer {token}'},
        json={'farmer_plan': 'pro'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['farmer_plan'] == 'pro'


def test_update_farmer_not_current_user(client, token, user, other_token):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.patch(
        f'/farmer/{response.json()['id']}',
        headers={'Authorization': f'Bearer {other_token}'},
        json={'farmer_plan': 'pro'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_update_farmer_not_exist(client, token):
    response = client.patch(
        '/farmer/1',
        headers={'Authorization': f'Bearer {token}'},
        json={'farmer_plan': 'pro'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Farmer does not exist'}


def test_delete_farmer(client, token, user):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.delete(
        f'/farmer/{response.json()['id']}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Farmer deleted'}


def test_delete_farmer_not_exist(client, token):
    response = client.delete(
        '/farmer/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    response.status_code == HTTPStatus.NOT_FOUND
    response.json() == {'detail': 'Farmer does not exist'}


def test_delete_farmer_not_current_user(client, token, user, other_token):
    response = client.post(
        '/farmer/',
        headers={'Authorization': f'Bearer {token}'},
        json={'user_id': user.id, 'farmer_plan': 'starter'},
    )

    response = client.delete(
        '/farmer/1',
        headers={'Authorization': f'Bearer {other_token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}
