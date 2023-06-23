from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserSchema, UserUpdate

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=UserSchema)
async def create(schema: UserCreate, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.create(**schema.dict(), user_type_id=1)
    await repository.commit()
    return db_user


@router.get("/{user_id}")
async def get_by(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.get(user_id)
    return db_user


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.get_all()
    return db_user


@router.patch("/{user_id}")
async def update(user_id: int, schema: UserUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.update(user_id, **schema.dict())
    await repository.commit()
    return db_user


@router.delete("/{user_id}")
async def delete(user_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = repository.delete(user_id)
    await repository.commit()
    return db_user
