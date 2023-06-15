from app.services.base import BaseService

from app.models.fazendeiro import Fazendeiro


class FazendeiroService(BaseService):
    def __init__(self):
        super().__init__(Fazendeiro)
