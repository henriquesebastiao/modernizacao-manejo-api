from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cargo import Cargo
from app.repositories.base import BaseRepository
from app.schemas.cargo import CargoSchema


class CargoRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Cargo, CargoSchema, db)
