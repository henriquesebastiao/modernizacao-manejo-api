from sqlalchemy.ext.asyncio import AsyncSession

from app.models.lote_log import LoteLog
from app.repositories.base import BaseRepository
from app.schemas.lote import LoteSchema


class LoteLogRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(LoteLog, LoteSchema, db)
