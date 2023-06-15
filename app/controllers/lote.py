from app.controllers.base import BaseControllers

from app.models.lote import Lote


class LoteController(BaseControllers):
    def __init__(self):
        super().__init__(Lote)
