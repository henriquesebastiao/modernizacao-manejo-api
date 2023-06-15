from app.controllers.base import BaseControllers

from app.models.animal import Animal


class AnimalController(BaseControllers):
    def __init__(self):
        super().__init__(Animal)
