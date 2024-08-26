from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models import Farmer
from app.schemas.farmer import FarmerCreate, FarmerSchema

router = APIRouter(prefix='/farmer', tags=['Farmer'])


@router.post('/', response_model=FarmerSchema, status_code=HTTPStatus.CREATED)
async def create(
    schema: FarmerCreate, db: AsyncSession = Depends(get_session)
):
    repository = Repository(Farmer, db)
    db_farmer = await repository.create(**schema.dict(), farmer_plan_id=1)
    await repository.commit()
    return db_farmer


@router.get('/{farmer_id}', response_model=FarmerSchema)
async def get_by(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = await repository.get(farmer_id)
    return db_farmer


@router.get('/', response_model=list[FarmerSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = await repository.get_all()
    return db_farmer


@router.patch('/{farmer_plan_id}', response_model=FarmerSchema)
async def update(
    farmer_plan_id: int,
    schema: FarmerSchema,
    db: AsyncSession = Depends(get_session),
):
    repository = Repository(Farmer, db)
    db_farmer = await repository.update(farmer_plan_id, **schema.dict())
    await repository.commit()
    return db_farmer


@router.delete('/{farmer_id}', response_model=FarmerSchema)
async def delete(farmer_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Farmer, db)
    db_farmer = repository.delete(farmer_id)
    await repository.commit()
    return db_farmer
