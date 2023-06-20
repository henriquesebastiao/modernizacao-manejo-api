from sqlalchemy.ext.asyncio import AsyncSession

from app.models.raca import Raca
from app.schemas.raca import RacaSchema
from app.repositories.base import BaseRepository


class RacaRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Raca, RacaSchema, db)
