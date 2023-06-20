from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dieta import Dieta
from app.repositories.base import BaseRepository
from app.schemas.dieta import DietaSchema


class DietaRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Dieta, DietaSchema, db)
