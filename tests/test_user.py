# from http import HTTPStatus

# import pytest


# @pytest.mark.asyncio
# async def test_create_user_deve_retornar_201(client):
#     response = await client.post(
#         '/user/',
#         json={
#             'first_name': 'Test',
#             'last_name': 'Pytest',
#             'email': 'test@pytest.com',
#             'password': 'segura123',
#             'user_type_id': 2
#         },
#     )

#     assert response.status_code == HTTPStatus.CREATED
