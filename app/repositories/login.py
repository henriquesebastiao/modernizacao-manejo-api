from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base import BaseRepository
from app.schemas.login import LoginSchema


class LoginRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(User, LoginSchema, db)

    async def login(self, login):
        user_db = await self.get_by_field("email", login.email)
        if user_db.password == login.password:
            return login
