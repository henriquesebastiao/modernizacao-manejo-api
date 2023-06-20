from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base import BaseRepository
from app.schemas.user import UserSchema


class UserRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(User, UserSchema, db)
