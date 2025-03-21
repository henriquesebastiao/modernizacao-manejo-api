import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from testcontainers.postgres import PostgresContainer

from app.core.database import get_session
from app.core.security import get_password_hash
from app.main import app
from app.models import table_registry
from tests.factories import AnimalFactory, UserFactory


@pytest.fixture(scope='session')
def engine():
    with PostgresContainer('postgres:17-alpine', driver='psycopg') as postgres:
        yield create_async_engine(postgres.get_connection_url())


@pytest.fixture
async def session(engine: AsyncEngine):
    async with engine.begin() as connection:
        await connection.run_sync(table_registry.metadata.create_all)

    async with AsyncSession(engine, expire_on_commit=False) as _session:
        yield _session

    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.drop_all)


@pytest.fixture
async def aclient(session: AsyncSession):
    async def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='https://test'
    ) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
async def user(session: AsyncSession):
    password = 'password'

    UserFactory.with_session(session)
    user = UserFactory(password=get_password_hash(password))
    session.add(user)
    await session.commit()
    await session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
async def other_user(session: AsyncSession):
    password = 'password'

    UserFactory._meta.sqlalchemy_session = session

    user = UserFactory(password=get_password_hash(password))
    session.add(user)
    await session.commit()
    await session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    return response.json()['access_token']


@pytest.fixture
def auth(token):
    return {'Authorization': f'Bearer {token}'}


@pytest.fixture
def other_token(client, other_user):
    response = client.post(
        '/token',
        data={
            'username': other_user.email,
            'password': other_user.clean_password,
        },
    )

    return response.json()['access_token']


@pytest.fixture
async def animal(session: AsyncSession):
    animal = AnimalFactory()
    session.add(animal)
    await session.commit()
    await session.refresh(animal)
    return animal
