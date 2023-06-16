from app.models.peso_log import PesoLog
from app.services.animal import AnimalService
from app.services.base import BaseService


class PesoLogService(BaseService):
    def __init__(self):
        super().__init__(PesoLog)

    def create(self, entity):
        db_animal = AnimalService().get_by_field("brinco", entity.ref)
        db_animal.peso = entity.peso
        peso_log = PesoLog(animal_id=db_animal.id, peso=entity.peso,
                                 data=entity.data)
        db_peso_log = super().create(peso_log)
        self.crud.commit()
        return db_peso_log
