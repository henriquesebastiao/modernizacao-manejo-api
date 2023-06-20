from sqlalchemy.ext.asyncio import AsyncSession

from app.models.fazenda import Fazenda
from app.repositories.base import BaseRepository
from app.schemas.fazenda import FazendaSchema


class FazendaRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Fazenda, FazendaSchema, db)
