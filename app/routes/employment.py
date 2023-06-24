from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.employment import Employment
from app.schemas.employment import EmploymentSchema

router = APIRouter(prefix="/employment",
                   tags=["Employment"])


@router.post("/", status_code=201)
async def create(schema: EmploymentSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, db)
    db_employment = await repository.create(**schema.dict())
    await repository.commit()
    return db_employment


@router.get("/{employment_id}")
async def get_by(employment_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, db)
    db_employment = await repository.get(employment_id)
    return db_employment


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, db)
    db_employment = await repository.get_all()
    return db_employment


@router.patch("/{employment_id}")
async def update(employment_id: int, schema: EmploymentSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, db)
    db_employment = await repository.update(employment_id, **schema.dict())
    await repository.commit()
    return db_employment


@router.delete("/{employment_id}")
async def delete(employment_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Employment, db)
    db_employment = repository.delete(employment_id)
    await repository.commit()
    return db_employment
