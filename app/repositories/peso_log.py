from sqlalchemy.ext.asyncio import AsyncSession

from app.models.peso_log import PesoLog
from app.repositories.base import BaseRepository
from app.schemas.peso_log import PesoLogSchema


class PesoLogRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(PesoLog, PesoLogSchema, db)
