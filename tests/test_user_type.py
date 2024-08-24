from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user_type(client: AsyncClient):
    response = await client.post(
        '/user/type/',
        json={'type': 'type_test'},
    )

    assert response.json() == {
        'id': 1,
        'type': 'type_test',
    }
    assert response.status_code == HTTPStatus.CREATED
