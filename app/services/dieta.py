from app.services.base import BaseService

from app.models.dieta import Dieta


class DietaService(BaseService):
    def __init__(self):
        super().__init__(Dieta)
