from datetime import datetime
from http import HTTPStatus


def test_get_all_animals(client, auth):
    response = client.get(
        '/animal/',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'animals': []}


def test_create_animal_with_all_atributes(client, auth):
    now = datetime.now().strftime('%Y-%m-%d')
    data = {
        'tag': 1,
        'sisbov': 1234,
        'gender': 'm',
        'birth_date': now,
        'buy_date': now,
        'breed': 'nelore',
        'origin': 'Fazenda de Teste',
    }

    response = client.post(
        '/animal/',
        headers=auth,
        json=data,
    )

    assert response.status_code == HTTPStatus.CREATED


def test_create_animal_without_optional_atributes(client, auth):
    response = client.post(
        '/animal/',
        headers=auth,
        json={
            'tag': 1,
            'gender': 'm',
            'breed': 'nelore',
        },
    )

    assert response.status_code == HTTPStatus.CREATED


def test_create_animal_already_exists(client, auth, animal):
    response = client.post(
        '/animal/',
        headers=auth,
        json={
            'tag': animal.tag,
            'gender': 'm',
            'breed': 'nelore',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Animal already exists'}


def test_update_animal(client, auth, animal):
    response = client.patch(
        f'/animal/{animal.tag}',
        headers=auth,
        json={'sisbov': 4321},
    )

    assert response.status_code == HTTPStatus.OK


def test_update_animal_not_found(client, auth):
    response = client.patch(
        '/animal/0',
        headers=auth,
        json={'sisbov': 4321},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Animal does not exist'}


def test_get_animal_by_tag(client, auth, animal):
    response = client.get(f'/animal/{animal.tag}', headers=auth)

    assert response.status_code == HTTPStatus.OK


def test_get_animal_by_tag_not_found(client, auth):
    response = client.get('/animal/0', headers=auth)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Animal does not exist'}


def test_delete_animal(client, auth, animal):
    response = client.delete(f'/animal/{animal.tag}', headers=auth)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Animal deleted'}


def test_delete_animal_not_found(client, auth):
    response = client.delete('/animal/0', headers=auth)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Animal does not exist'}
