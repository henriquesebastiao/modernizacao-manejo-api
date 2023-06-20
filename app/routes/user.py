from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.user import UserCreate, UserSchema, UserUpdate
from app.repositories.user import UserRepository

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=201)
async def create(cargo: UserCreate, db: AsyncSession = Depends(get_session)):
    repository = UserRepository(db)
    return await repository.create(cargo)


@router.get("/{user_id}", response_model=UserSchema)
async def get_by_id(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = UserRepository(db)
    return await repository.get_by_id(user_id)


@router.get("/", response_model=list[UserSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = UserRepository(db)
    return await repository.get_all()


@router.patch("/{user_id}")
async def update(user_id: int, user: UserUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = UserRepository(db)
    return await repository.update(user_id, user)


@router.delete("/{user_id}")
async def delete(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = UserRepository(db)
    return repository.delete(user_id)
