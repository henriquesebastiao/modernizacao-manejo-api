from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user import User
from app.schemas.login import LoginSchema
from app.schemas.user import UserSchema

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/")
async def email(schema: LoginSchema, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.get(schema.email, "email")
    if not db_user:
        return None
    if db_user.password != schema.password:
        return None
    else:
        return db_user
