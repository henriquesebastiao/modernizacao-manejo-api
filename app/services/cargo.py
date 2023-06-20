from app.models.cargo import Cargo
from app.schemas.cargo import CargoSchema
from app.services.base import BaseService


class CargoService(BaseService):
    def __init__(self, session):
        super().__init__(Cargo, CargoSchema, session)
