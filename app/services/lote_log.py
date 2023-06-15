from app.services.base import BaseService

from app.models.lote_log import LoteLog


class LoteLogService(BaseService):
    def __init__(self):
        super().__init__(LoteLog)
