from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.employment import Employment
from app.schemas.employment import EmploymentSchema

router = APIRouter(prefix="/animal/weight",
                   tags=["Animal Weight"])


@router.post("/")
async def create(user: EmploymentSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, EmploymentSchema, db)
    return await repository.create(user)


@router.get("/{employment_id}")
async def get_by(employment_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, EmploymentSchema, db)
    return await repository.get(employment_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, EmploymentSchema, db)
    return await repository.get_all()


@router.patch("/{employment_id}")
async def update(employment_id: int, user: EmploymentSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, EmploymentSchema, db)
    return await repository.update(employment_id, user)


@router.delete("/{employment_id}")
async def delete(employment_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, EmploymentSchema, db)
    return repository.delete(employment_id)
