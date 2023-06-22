from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.employment_position import EmploymentPosition
from app.schemas.employment_position import EmploymentPositionSchema

router = APIRouter(prefix="/employment/position",
                   tags=["Employment Position"])


@router.post("/")
async def create(schema: EmploymentPositionSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    db_employment_position = await repository.create(schema)
    await repository.commit()
    return db_employment_position


@router.get("/{employment_position_id}")
async def get_by(employment_position_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    db_employment_position = await repository.get(employment_position_id)
    return db_employment_position


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    db_employment_position = await repository.get_all()
    return db_employment_position


@router.patch("/{employment_position_id}")
async def update(employment_position_id: int, user: EmploymentPositionSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    db_employment_position = await repository.update(employment_position_id,
                                                     user)
    await repository.commit()
    return db_employment_position


@router.delete("/{employment_position_id}")
async def delete(employment_position_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(EmploymentPosition, EmploymentPositionSchema, db)
    db_employment_position = repository.delete(employment_position_id)
    await repository.commit()
    return db_employment_position
