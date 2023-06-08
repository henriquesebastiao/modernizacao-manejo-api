from typing import Type, TypeVar

from sqlalchemy.orm import Session

from app.models.lote_log import LoteLog
from app.models.peso_log import PesoLog
from app.repositories.repository import BaseRepository
from app.schemas.animal import AnimalCreateSchema
from app.schemas.lote_log import LoteLogCreateSchema
from app.schemas.peso_log import PesoLogCreateSchema
from app.services.base_service import BaseService

T = TypeVar('T')


class AnimalService(BaseService):
    def __init__(self, db: Session, model: Type[T] = None):
        super().__init__(db, model)

    def create(self, animal: AnimalCreateSchema) -> bool:
        """
        Cria um animal.

        Args:
            animal (AnimalCreate): Os dados do animal a ser criado.

        Returns:
            Animal: O animal criado.
        """
        try:
            entity = self.model(**animal.dict())
            BaseRepository(self.db, self.model).create(entity)
            service_peso_log = BaseService(self.db, PesoLog)
            peso_log = PesoLogCreateSchema(animal_id=entity.id,
                                           data=animal.data_entrada,
                                           peso=animal.peso)
            service_peso_log.create(peso_log)

            service_lote_log = BaseService(self.db, LoteLog)
            lote_log = LoteLogCreateSchema(animal_id=entity.id,
                                           lote_id=entity.lote_id,
                                           data_entrada=entity.data_entrada)
            service_lote_log.create(lote_log)
        except Exception:
            return False
        return True
