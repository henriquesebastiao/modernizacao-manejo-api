from datetime import datetime
from http import HTTPStatus


def test_create_animal_weight(client, auth):
    response = client.post(
        '/animal/weight/',
        headers=auth,
        json={
            'weight_type': 'weaning',
            'animal_tag': 1,
            'weight': 150.2,
            'weight_date': str(datetime.now()),
        },
    )

    assert response.status_code == HTTPStatus.CREATED


def test_create_animal_weight_with_invalid_weight_type(client, auth):
    response = client.post(
        '/animal/weight/',
        headers=auth,
        json={
            'weight_type': 'invalid',
            'animal_tag': 1,
            'weight': 150.2,
            'weight_date': str(datetime.now()),
        },
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_get_animal_weight_by_id(client, auth, animal_weight):
    response = client.get(
        f'/animal/weight/{animal_weight.id}',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['weight'] == 150.0


def test_get_animal_weight_by_id_not_exists(client, auth):
    response = client.get(
        '/animal/weight/0',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Weight not exists'}


def test_get_all_animal_weight(client, auth):
    response = client.get('/animal/weight/', headers=auth)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'animal_weights': []}


def test_update_animal_weight(client, auth, animal_weight):
    response = client.patch(
        f'/animal/weight/{animal_weight.id}',
        headers=auth,
        json={'weight': 160.0},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['weight'] == 160.0


def test_update_animal_weight_not_exists(client, auth):
    response = client.patch(
        '/animal/weight/0', headers=auth, json={'weight': 170.0}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Weight not exists'}


def test_delete_animal_weight(client, auth, animal_weight):
    response = client.delete(
        f'/animal/weight/{animal_weight.id}',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK


def test_delete_animal_weight_not_exists(client, auth):
    response = client.delete(
        '/animal/weight/0',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Weight not exists'}
