from sqlalchemy.ext.asyncio import AsyncSession

from app.models.lote import Lote
from app.repositories.base import BaseRepository
from app.schemas.lote import LoteSchema


class LoteRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Lote, LoteSchema, db)
