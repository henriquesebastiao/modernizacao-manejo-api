from app.services.base import BaseService

from app.models.propriedade import Propriedade


class PropriedadeService(BaseService):
    def __init__(self):
        super().__init__(Propriedade)
