from app.services.base import BaseService

from app.models.fazenda import Fazenda


class FazendaService(BaseService):
    def __init__(self):
        super().__init__(Fazenda)
