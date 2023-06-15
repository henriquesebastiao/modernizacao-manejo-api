from app.controllers.base import BaseControllers

from app.models.fazendeiro import Fazendeiro


class FazendeiroController(BaseControllers):
    def __init__(self):
        super().__init__(Fazendeiro)
