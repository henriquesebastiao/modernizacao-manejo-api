from app.schemas.login import LoginSchema
from app.services.base import BaseService

from app.models.user import User


class LoginService(BaseService):
    def __init__(self, session):
        super().__init__(User, LoginSchema, session)

    async def login(self, login):
        user_db = await self.get_by_field("email", login.email)
        if user_db.password == login.password:
            return login
