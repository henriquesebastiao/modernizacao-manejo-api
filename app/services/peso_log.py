from app.services.base import BaseService

from app.models.peso_log import PesoLog


class PesoLogService(BaseService):
    def __init__(self):
        super().__init__(PesoLog)
