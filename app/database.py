from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import Settings

engine = create_async_engine(Settings().DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
