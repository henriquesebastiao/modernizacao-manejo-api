from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user import User
from app.schemas.user import UserSchema

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/")
async def create(user: UserSchema, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, UserSchema, db)
    return await repository.create(user)


@router.get("/{user_id}")
async def get_by_id(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, UserSchema, db)
    return await repository.get(user_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(User, UserSchema, db)
    return await repository.get_all()


@router.patch("/{user_id}")
async def update(user_id: int, user: UserSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(User, UserSchema, db)
    return await repository.update(user_id, user)


@router.delete("/{user_id}")
async def delete(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, UserSchema, db)
    return repository.delete(user_id)
