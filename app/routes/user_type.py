from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user_type import UserType
from app.schemas.user_type import UserTypeCreate, UserTypeSchema, UserTypeUpdate

router = APIRouter(prefix="/user/type", tags=["User Type"])


@router.post("/", response_model=UserTypeSchema, status_code=201)
async def create(schema: UserTypeCreate,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, db)
    db_user_type = await repository.create(**schema.dict())
    await repository.commit()
    return db_user_type


@router.get("/{user_type_id}", response_model=UserTypeSchema)
async def get_by(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, db)
    db_user_type = await repository.get(user_type_id)
    return db_user_type


@router.get("/", response_model=list[UserTypeSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, db)
    db_user_type = await repository.get_all()
    return db_user_type


@router.patch("/{user_type_id}", response_model=UserTypeSchema)
async def update(user_type_id: int, user: UserTypeUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, db)
    db_user_type = await repository.update(user_type_id, user)
    await repository.commit()
    return db_user_type


@router.delete("/{user_type_id}", response_model=UserTypeSchema)
async def delete(user_type_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(UserType, db)
    db_user_type = await repository.delete(user_type_id)
    await repository.commit()
    return db_user_type
