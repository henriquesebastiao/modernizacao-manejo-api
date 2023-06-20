from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.login import LoginSchema
from app.repositories.login import LoginRepository

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", status_code=200)
async def login(user: LoginSchema, db: AsyncSession = Depends(get_session)):
    repository = LoginRepository(db)
    return await repository.login(user)

