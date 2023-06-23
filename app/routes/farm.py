from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.farm import Farm
from app.schemas.farm import FarmSchema

router = APIRouter(prefix="/farm", tags=["Farm"])


@router.post("/")
async def create(schema: FarmSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, db)
    db_farm = await repository.create(**schema.dict())
    await repository.commit()
    return db_farm


@router.get("/{farm_id}")
async def get_by(farm_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, db)
    db_farm = await repository.get(farm_id)
    return db_farm


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, db)
    db_farm = await repository.get_all()
    return db_farm


@router.patch("/{farm_id}")
async def update(farm_id: int, schema: FarmSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, db)
    db_farm = await repository.update(farm_id, **schema.dict())
    await repository.commit()
    return db_farm


@router.delete("/{farm_id}")
async def delete(farm_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farm, db)
    db_farm = repository.delete(farm_id)
    await repository.commit()
    return db_farm
