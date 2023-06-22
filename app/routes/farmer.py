from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerSchema

router = APIRouter(prefix="/farmer", tags=["Farmer"])


@router.post("/")
async def create(user: FarmerSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, FarmerSchema, db)
    return await repository.create(user)


@router.get("/{farmer_id}")
async def get_by(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, FarmerSchema, db)
    return await repository.get(farmer_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, FarmerSchema, db)
    return await repository.get_all()


@router.patch("/{farmer_plan_id}")
async def update(farmer_plan_id: int, user: FarmerSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, FarmerSchema, db)
    return await repository.update(farmer_plan_id, user)


@router.delete("/{farmer_id}")
async def delete(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, FarmerSchema, db)
    return repository.delete(farmer_id)
