from app.schemas.user import UserSchema
from app.services.base import BaseService

from app.models.user import User


class UserService(BaseService):
    def __init__(self, session):
        super().__init__(User, UserSchema, session)
