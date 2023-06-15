from app.services.base import BaseService

from app.models.lote import Lote


class LoteService(BaseService):
    def __init__(self):
        super().__init__(Lote)
