from typing import Any, Sequence

from sqlalchemy import Row, RowMapping, select
from sqlalchemy.orm import Session

from app.models.base import Base


class BaseRepository:
    def __init__(self, db: Session, model: Base):
        self.db: Session = db
        self.model: Base = model

    def create(self, entity: Base) -> bool:
        try:
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def update(self, entity: Base) -> bool:
        try:
            self.db.commit()
            self.db.refresh(entity)
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def delete(self, entity: Base) -> bool:
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def get_all(self) -> list[Base]:
        try:
            entity = self.db.query(self.model).all()
        except Exception:
            raise Exception
        return entity

    def get_by_id(self, entity_id: int) -> Base:
        try:
            stmt = select(self.model).where(self.model.id == entity_id)
            entity = self.db.execute(stmt).scalar()
            if not entity:
                raise Exception
        except Exception:
            raise Exception
        return entity

    def get_by_field(self, field_name: str, value: str) \
            -> Sequence[Row | RowMapping | Any]:
        try:
            stmt = select(self.model).where(
                getattr(self.model, field_name) == value)
            entity = self.db.execute(stmt).scalars().all()
            if not entity:
                raise Exception
        except Exception:
            raise Exception
        return entity
