from http import HTTPStatus


def test_create_breed(client, auth):
    response = client.post(
        '/animal/breed/',
        headers=auth,
        json={'name': 'Raca das Vaquinhas Festivas'},
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'id': 1, 'name': 'Raca das Vaquinhas Festivas'}


def test_create_breed_already_exists(client, auth, breed):
    response = client.post(
        '/animal/breed/', headers=auth, json={'name': breed.name}
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Breed already exists'}


def test_get_all_breeds(client, auth, breed):
    response = client.get(
        '/animal/breed/',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'breeds': [{'id': 1, 'name': breed.name}]}


def test_update_breed(client, auth, breed):
    response = client.patch(
        f'/animal/breed/{breed.name}',
        headers=auth,
        json={'name': 'raca nova para as vaquinhas festivas'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 'raca nova para as vaquinhas festivas',
    }


def test_update_breed_not_found(client, auth):
    response = client.patch(
        '/animal/breed/raca_nao_existe',
        headers=auth,
        json={'name': 'raca nova para as vaquinhas festivas'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Breed not found'}


def test_delete_breed(client, auth, breed):
    response = client.delete(
        f'/animal/breed/{breed.name}',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Breed deleted'}


def test_delete_breed_not_found(client, auth):
    response = client.delete(
        '/animal/breed/raca_nao_existe',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Breed not found'}
