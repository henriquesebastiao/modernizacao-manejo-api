from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerSchema, FarmerCreate

from app.models.user import User

router = APIRouter(prefix="/farmer", tags=["Farmer"])


@router.post("/", response_model=FarmerSchema)
async def create(schema: FarmerCreate,
                 db: AsyncSession = Depends(get_session)):
    repository_user = Repository(User, db)
    db_user = await repository_user.create(**schema.dict(), user_type_id=2)
    repository = Repository(Farmer, db)
    db_farmer = await repository.create(user_id=db_user.id, farmer_plan_id=1)
    await repository.commit()
    return db_farmer


@router.get("/{farmer_id}")
async def get_by(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = await repository.get(farmer_id)
    return db_farmer


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = await repository.get_all()
    return db_farmer


@router.patch("/{farmer_plan_id}")
async def update(farmer_plan_id: int, user: FarmerSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = await repository.update(farmer_plan_id, user)
    await repository.commit()
    return db_farmer


@router.delete("/{farmer_id}")
async def delete(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = repository.delete(farmer_id)
    await repository.commit()
    return db_farmer
