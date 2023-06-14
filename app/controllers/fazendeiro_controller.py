from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.models.base import Base
from app.models.user import User
from app.repositories.repository import BaseRepository
from app.schemas.fazendeiro import FazendeiroCreateSchema
from app.schemas.user import UserCreateSchema


class FazendeiroController(BaseControllers):
    def __init__(self, db: Session, model: Base):
        super().__init__(db, model)

    def create(self, fazendeiro: FazendeiroCreateSchema) -> bool:
        try:
            entity = self.model(**fazendeiro.dict())
            BaseRepository(self.db, self.model).create(entity)
            controllers_user = BaseControllers(self.db, User)
            user = UserCreateSchema(email=entity.email,
                                    password=entity.password,
                                    )
            controllers_user.create(user)
        except Exception:
            return False
        return True
