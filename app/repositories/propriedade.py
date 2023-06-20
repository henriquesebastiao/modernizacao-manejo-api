from sqlalchemy.ext.asyncio import AsyncSession

from app.models.propriedade import Propriedade
from app.repositories.base import BaseRepository
from app.schemas.propriedade import PropriedadeSchema


class PropriedadeRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Propriedade, PropriedadeSchema, db)
