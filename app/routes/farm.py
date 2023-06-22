from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.farm import Farm
from app.schemas.farm import FarmSchema

router = APIRouter(prefix="/farmer", tags=["Farmer"])


@router.post("/")
async def create(user: FarmSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, FarmSchema, db)
    return await repository.create(user)


@router.get("/{farm_id}")
async def get_by(farm_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, FarmSchema, db)
    return await repository.get(farm_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, FarmSchema, db)
    return await repository.get_all()


@router.patch("/{farm_id}")
async def update(farm_id: int, user: FarmSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, FarmSchema, db)
    return await repository.update(farm_id, user)


@router.delete("/{farm_id}")
async def delete(farm_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, FarmSchema, db)
    return repository.delete(farm_id)
