from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class Repository:
    def __init__(self, model, db: AsyncSession):
        self.model = model
        self.session: AsyncSession = db

    async def commit(self):
        await self.session.commit()

    async def create(self, entity, **kwargs):
        stmt = insert(self.model).values(**entity.dict(), **kwargs)
        db_value = await self.session.scalar(stmt.returning(self.model))
        return db_value

    async def update(self, value_id: int, new_value):
        stmt = update(self.model).where(self.model.id == value_id).values(
            **new_value.dict())
        db_value = await self.session.scalar(stmt.returning(self.model))
        return db_value

    async def delete(self, value_id: int):
        stmt = delete(self.model).where(self.model.id == value_id)
        db_value = await self.session.scalar(stmt.returning(self.model))
        return db_value

    async def get(self, value: str | int, field_name: str = "id"):
        stmt = select(self.model).where(
            getattr(self.model, field_name) == value)
        db_value = await self.session.scalar(stmt)
        return db_value

    async def get_all(self):
        stmt = select(self.model)
        db_value = await self.session.scalars(stmt)
        return db_value.all()
