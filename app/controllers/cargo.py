from app.controllers.base_controller import BaseControllers

from app.models.cargo import Cargo


class CargoController(BaseControllers):
    def __init__(self):
        super().__init__(Cargo)
