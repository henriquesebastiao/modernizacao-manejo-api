from app.controllers.base import BaseControllers

from app.models.peso_log import PesoLog


class PesoLogController(BaseControllers):
    def __init__(self):
        super().__init__(PesoLog)
