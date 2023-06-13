from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.models.base import Base
from app.models.lote_log import LoteLog
from app.models.peso_log import PesoLog
from app.repositories.repository import BaseRepository
from app.schemas.animal import AnimalCreateSchema
from app.schemas.lote_log import LoteLogCreateSchema
from app.schemas.peso_log import PesoLogCreateSchema


class AnimalController(BaseControllers):
    def __init__(self, db: Session, model: Base):
        super().__init__(db, model)

    def create(self, animal: AnimalCreateSchema) -> bool:
        try:
            entity = self.model(**animal.dict())
            BaseRepository(self.db, self.model).create(entity)
            controllers_peso_log = BaseControllers(self.db, PesoLog)
            peso_log = PesoLogCreateSchema(animal_id=entity.id,
                                           data=animal.data_entrada,
                                           peso=animal.peso)
            controllers_peso_log.create(peso_log)

            controllers_lote_log = BaseControllers(self.db, LoteLog)
            lote_log = LoteLogCreateSchema(animal_id=entity.id,
                                           lote_id=entity.lote_id,
                                           data_entrada=entity.data_entrada)
            controllers_lote_log.create(lote_log)
        except Exception:
            return False
        return True
