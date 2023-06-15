from app.controllers.base import BaseControllers

from app.models.propriedade import Propriedade


class PropriedadeController(BaseControllers):
    def __init__(self):
        super().__init__(Propriedade)
