from sqlalchemy import select

from app.database import SessionLocal


class CRUD:
    def __init__(self, model):
        self.model = model
        self.db = SessionLocal()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def refresh(self, entity):
        self.db.refresh(entity)

    def create(self, entity):
        self.db.add(entity)

    def update(self, entity):
        self.db.refresh(entity)

    def delete(self, entity):
        self.db.delete(entity)

    def get_by(self, field_name, value):
        stmt = select(self.model).where(getattr(self.model, field_name) == value)
        return self.db.scalar(stmt)

    def get_all_by(self, field_name, value):
        stmt = select(self.model).where(
            getattr(self.model, field_name) == value)
        return self.db.scalars(stmt)
