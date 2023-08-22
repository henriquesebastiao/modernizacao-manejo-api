from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{settings.db_user}:{settings.db_password}@'
    f'{settings.db_host}:{settings.db_port}/{settings.db_name}'
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
