from app.controllers.base import BaseControllers

from app.models.cargo import Cargo


class CargoController(BaseControllers):
    def __init__(self):
        super().__init__(Cargo)
