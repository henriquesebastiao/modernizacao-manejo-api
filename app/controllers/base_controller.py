from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models.base import Base
from app.repositories.repository import BaseRepository


class BaseControllers:
    def __init__(self, db: Session, model: Base):
        self.db: Session = db
        self.model: Base = model

    def create(self, entity: BaseModel) -> bool:
        try:
            if entity := self.model(**entity.dict()):
                BaseRepository(self.db, self.model).create(entity)
        except Exception:
            return False
        return True

    def update(self, entity_id: int, entity: BaseModel) -> bool:
        try:
            db_entity = BaseRepository(self.db, self.model).get_by_id(entity_id)
            if db_entity:
                for field, value in entity.dict(exclude_unset=True).items():
                    setattr(db_entity, field, value)
                    BaseRepository(self.db, self.model).update(
                        db_entity)
        except Exception:
            return False
        return True

    def delete(self, entity_id: int) -> bool:
        try:
            db_entity = BaseRepository(self.db, self.model).get_by_id(entity_id)
            if db_entity:
                BaseRepository(self.db, self.model).delete(db_entity)
        except Exception:
            return False
        return True

    def get_all(self) -> list[Base] | None:
        try:
            db_entity = BaseRepository(self.db, self.model).get_all()
        except Exception:
            return None
        return db_entity

    def get_by_id(self, entity_id: int) -> Base | None:
        try:
            db_entity = BaseRepository(self.db, self.model).get_by_id(entity_id)
        except Exception:
            return None
        return db_entity

    def get_by_field(self, field_name: str, value: str) -> list[Base] | None:
        try:
            db_entity = BaseRepository(self.db, self.model).get_by_field(
                field_name, value)
        except Exception:
            return None
        return db_entity
