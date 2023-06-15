from app.services.base import BaseService

from app.models.raca import Raca


class RacaService(BaseService):
    def __init__(self):
        super().__init__(Raca)
