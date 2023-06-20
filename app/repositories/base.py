from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class BaseRepository:
    def __init__(self, model, schema, db: AsyncSession):
        self.model = model
        self.schema = schema
        self.session: AsyncSession = db

    async def create(self, entity):
        entity = self.schema.parse_obj(entity)
        entity_orm = self.model(**entity.dict())
        self.session.add(entity_orm)
        await self.session.commit()

    async def update(self, value_id, new_value):
        db_value = await self.get_by_id(value_id)
        if db_value:
            new_value = self.schema.parse_obj(new_value)
            for field, value in new_value.dict().items():
                setattr(db_value, field, value)
            await self.session.commit()
            return {"message": "Registro atualizado com sucesso!"}
        return {"message": "Registro não encontrado!"}

    async def delete(self, value_id):
        db_value = await self.get_by_id(value_id)
        if db_value:
            await self.session.delete(db_value)
            await self.session.commit()
            return {"message": "Registro excluído com sucesso!"}
        return {"message": "Registro não encontrado!"}

    async def get_by_id(self, value_id: int):
        stmt = select(self.model).where(self.model.id == value_id)
        db_value = await self.session.scalar(stmt)
        return db_value

    async def get_by_field(self, field_name: str, value: str | int):
        stmt = select(self.model).where(
            getattr(self.model, field_name) == value)
        db_value = await self.session.scalar(stmt)
        return db_value

    async def get_all(self):
        stmt = select(self.model)
        db_value = await self.session.scalars(stmt)
        return db_value.all()

    async def get_all_by_field(self, field_name, value: str | int):
        stmt = select(self.model).where(
            getattr(self.model, field_name) == value)
        db_value = await self.session.scalars(stmt)
        return db_value.all()
