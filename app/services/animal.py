from app.services.base import BaseService

from app.models.animal import Animal


class AnimalService(BaseService):
    def __init__(self):
        super().__init__(Animal)
