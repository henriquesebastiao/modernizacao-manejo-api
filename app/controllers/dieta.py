from app.controllers.base import BaseControllers

from app.models.dieta import Dieta


class DietaController(BaseControllers):
    def __init__(self):
        super().__init__(Dieta)
