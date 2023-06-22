from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.employment_position import EmploymentPosition
from app.schemas.employment_position import EmploymentPositionSchema

router = APIRouter(prefix="/employment/position",
                   tags=["Employment Position"])


@router.post("/")
async def create(user: EmploymentPositionSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    return await repository.create(user)


@router.get("/{employment_position_id}")
async def get_by_id(employment_position_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    return await repository.get(employment_position_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    return await repository.get_all()


@router.patch("/{employment_position_id}")
async def update(employment_position_id: int, user: EmploymentPositionSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    return await repository.update(employment_position_id, user)


@router.delete("/{employment_position_id}")
async def delete(employment_position_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    return repository.delete(employment_position_id)
