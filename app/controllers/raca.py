from app.controllers.base import BaseControllers

from app.models.raca import Raca


class RacaController(BaseControllers):
    def __init__(self):
        super().__init__(Raca)
