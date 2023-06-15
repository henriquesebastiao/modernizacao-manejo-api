from app.services.base import BaseService

from app.models.cargo import Cargo


class CargoService(BaseService):
    def __init__(self):
        super().__init__(Cargo)
