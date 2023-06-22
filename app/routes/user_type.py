from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user_type import UserType
from app.schemas.user_type import UserTypeSchema

router = APIRouter(prefix="/user/type", tags=["User Type"])


@router.post("/")
async def create(user: UserTypeSchema, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    return await repository.create(user)


@router.get("/{user_type_id}")
async def get_by_id(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    return await repository.get(user_type_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    return await repository.get_all()


@router.patch("/{user_type_id}")
async def update(user_type_id: int, user: UserTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    return await repository.update(user_type_id, user)


@router.delete("/{user_type_id}")
async def delete(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    return repository.delete(user_type_id)
