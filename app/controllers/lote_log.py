from app.controllers.base import BaseControllers

from app.models.lote_log import LoteLog


class LoteLogController(BaseControllers):
    def __init__(self):
        super().__init__(LoteLog)
