from http import HTTPStatus

from jwt import decode

from app.core.security import (
    create_access_token,
    get_password_hash,
    verify_password,
)
from app.core.settings import get_settings

settings = get_settings()


def test_jwt():
    data = {'sub': 'user@test.com'}
    token = create_access_token(data)

    result = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert result['sub'] == data['sub']
    assert result['exp']  # Testa se o valor de exp foi adicionado ao token


def test_jwt_invalid_token(client, user):
    response = client.delete(
        f'/user/{user.id}', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_valid_token_with_user_not_exists(client, auth, user):
    client.delete(
        f'/user/{user.id}',
        headers=auth,
    )

    response = client.delete(
        f'/user/{user.id}',
        headers=auth,
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_verify_password():
    plain_text = 'password'
    pwd_hash = get_password_hash(plain_text)

    assert verify_password(plain_text, pwd_hash)
