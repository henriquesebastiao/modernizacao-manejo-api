from app.models.animal import Animal
from app.schemas.animal import AnimalSchema
from app.services.base import BaseService


class AnimalService(BaseService):
    def __init__(self, session):
        super().__init__(Animal, AnimalSchema, session)
