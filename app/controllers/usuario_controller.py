from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.models.base import Base
from app.repositories.repository import BaseRepository
from app.schemas.user import UserLoginSchema


class UserController(BaseControllers):
    def __init__(self, db: Session, model: Base):
        super().__init__(db, model)

    def login(self, user: UserLoginSchema) -> bool:
        try:
            user_db = BaseRepository(self.db, self.model).get_by_field(
                "email", user.email)
            if user_db is None:
                raise Exception
            if user_db[0].password != user.password:
                raise Exception
        except Exception:
            return False
        return True

    def register(self, user: UserLoginSchema) -> bool:
        try:
            user_db = BaseRepository(self.db, self.model).get_by_field(
                "email", user.email)
            if user_db is None:
                raise Exception
            if user_db[0].password != user.password:
                raise Exception
        except Exception:
            return False
        return True
