from sqlalchemy.ext.asyncio import AsyncSession

from app.models.animal import Animal
from app.repositories.base import BaseRepository
from app.schemas.animal import AnimalSchema


class AnimalRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Animal, AnimalSchema, db)
