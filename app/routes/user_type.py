from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user_type import UserType
from app.schemas.user_type import UserTypeSchema

router = APIRouter(prefix="/user/type", tags=["User Type"])


@router.post("/")
async def create(schema: UserTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    db_user_type = await repository.create(schema)
    await repository.commit()
    return db_user_type


@router.get("/{user_type_id}")
async def get_by(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    db_user_type = await repository.get(user_type_id)
    return db_user_type


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    db_user_type = await repository.get_all()
    return db_user_type


@router.patch("/{user_type_id}")
async def update(user_type_id: int, user: UserTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    db_user_type = await repository.update(user_type_id, user)
    await repository.commit()
    return db_user_type


@router.delete("/{user_type_id}")
async def delete(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, UserTypeSchema, db)
    db_user_type = repository.delete(user_type_id)
    await repository.commit()
    return db_user_type
