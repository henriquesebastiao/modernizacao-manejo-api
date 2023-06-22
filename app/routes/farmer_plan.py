from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.farmer_plan import FarmerPlan
from app.schemas.farmer_plan import FarmerPlanSchema

router = APIRouter(prefix="/farmer/plan", tags=["Farmer plan"])


@router.post("/")
async def create(user: FarmerPlanSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(FarmerPlan, FarmerPlanSchema, db)
    return await repository.create(user)


@router.get("/{farmer_plan_id}")
async def get_by_id(farmer_plan_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(FarmerPlan, FarmerPlanSchema, db)
    return await repository.get(farmer_plan_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(FarmerPlan, FarmerPlanSchema, db)
    return await repository.get_all()


@router.patch("/{farmer_plan_id}")
async def update(farmer_plan_id: int, user: FarmerPlanSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(FarmerPlan, FarmerPlanSchema, db)
    return await repository.update(farmer_plan_id, user)


@router.delete("/{farmer_plan_id}")
async def delete(farmer_plan_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(FarmerPlan, FarmerPlanSchema, db)
    return repository.delete(farmer_plan_id)
