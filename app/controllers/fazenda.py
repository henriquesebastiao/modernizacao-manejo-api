from app.controllers.base import BaseControllers

from app.models.fazenda import Fazenda


class FazendaController(BaseControllers):
    def __init__(self):
        super().__init__(Fazenda)
