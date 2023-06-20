from sqlalchemy.ext.asyncio import AsyncSession

from app.models.fazendeiro import Fazendeiro
from app.repositories.base import BaseRepository
from app.schemas.fazendeiro import FazendeiroSchema


class FazendeiroRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Fazendeiro, FazendeiroSchema, db)
