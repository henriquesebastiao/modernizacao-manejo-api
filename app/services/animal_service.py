from typing import Type, TypeVar

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.peso_log import PesoLog
from app.repository import BaseRepository
from app.schemas.animal import AnimalCreateSchema
from app.schemas.peso_log import PesoLogCreateSchema
from app.services.base_service import BaseService

T = TypeVar('T')


class AnimalService(BaseService):
    def __init__(self, db: Session, model: Type[T] = None):
        super().__init__(db, model)

    def create(self, animal: AnimalCreateSchema) -> Animal | None:
        """
        Cria um animal.

        Args:
            animal (AnimalCreate): Os dados do animal a ser criado.

        Returns:
            Animal: O animal criado.
        """
        entity = self.model(**animal.dict())
        BaseRepository(self.db, self.model).create(entity)
        service_peso_log = BaseService(self.db, PesoLog)
        peso_log = PesoLogCreateSchema(animal_id=entity.id,
                                       data=animal.data_entrada,
                                       peso=animal.peso)
        service_peso_log.create(peso_log)
        return entity
