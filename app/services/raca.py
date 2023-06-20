from app.models.raca import Raca
from app.schemas.raca import RacaSchema
from app.services.base import BaseService


class RacaService(BaseService):
    def __init__(self, session):
        super().__init__(Raca, RacaSchema, session)
