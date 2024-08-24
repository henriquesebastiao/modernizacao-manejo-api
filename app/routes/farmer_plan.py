from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models import FarmerPlan
from app.schemas.farmer import FarmerPlanSchema

router = APIRouter(prefix='/farmer/plan', tags=['Farmer plan'])


@router.post('/', status_code=201)
async def create(
    schema: FarmerPlanSchema, db: AsyncSession = Depends(get_session)
):
    """
    Adiciona um plano de assinatura para o agricultor

    - **plan (str)**: Nome do plano de assinatura
    """
    repository = Repository(FarmerPlan, db)
    await repository.commit()
    db_farmer_plan = await repository.create(**schema.dict())
    return db_farmer_plan


@router.get('/{farmer_plan_id}')
async def get_by(farmer_plan_id: int, db: AsyncSession = Depends(get_session)):
    """Retorna um plano de assinatura pelo ID."""
    repository = Repository(FarmerPlan, db)
    db_farmer_plan = await repository.get(farmer_plan_id)
    return db_farmer_plan


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todos os planos de assinatura."""
    repository = Repository(FarmerPlan, db)
    db_farmer_plan = await repository.get_all()
    return db_farmer_plan


@router.patch('/{farmer_plan_id}')
async def update(
    farmer_plan_id: int,
    schema: FarmerPlanSchema,
    db: AsyncSession = Depends(get_session),
):
    """
    Atualiza um plano de assinatura pelo ID.

    - **plan (str)**: Nome do plano de assinatura
    """
    repository = Repository(FarmerPlan, db)
    await repository.commit()
    db_farmer_plan = await repository.update(farmer_plan_id, **schema.dict())
    return db_farmer_plan


@router.delete('/{farmer_plan_id}')
async def delete(farmer_plan_id: int, db: AsyncSession = Depends(get_session)):
    """Deleta um plano de assinatura pelo ID."""
    repository = Repository(FarmerPlan, db)
    await repository.commit()
    db_farmer_plan = repository.delete(farmer_plan_id)
    return db_farmer_plan
