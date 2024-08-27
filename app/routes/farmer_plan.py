from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import FarmerPlan
from app.schemas.farmer import FarmerPlanList, FarmerPlanSchema
from app.utils import T_Session

router = APIRouter(prefix='/farmer/plan', tags=['Farmer plan'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=FarmerPlanSchema
)
async def create(schema: FarmerPlanSchema, session: T_Session):
    db_farmer_plan = FarmerPlan(**schema.model_dump())

    session.add(db_farmer_plan)
    await session.commit()
    await session.refresh(db_farmer_plan)

    return db_farmer_plan


@router.get('/{farmer_plan_id}', response_model=FarmerPlanSchema)
async def get_by_id(farmer_plan_id: int, session: T_Session):
    db_farmer_plan = await session.scalar(
        select(FarmerPlan).where(FarmerPlan.id == farmer_plan_id)
    )

    return db_farmer_plan


@router.get('/', response_model=FarmerPlanList)
async def get_all(session: T_Session):
    db_farmer_plan = await session.scalars(select(FarmerPlan))

    return {'farmer_plans': db_farmer_plan.all()}


@router.patch('/{farmer_plan_id}', response_model=FarmerPlanSchema)
async def update(
    farmer_plan_id: int,
    schema: FarmerPlanSchema,
    session: T_Session,
):
    query = (
        up(FarmerPlan)
        .where(FarmerPlan.id == farmer_plan_id)
        .values(**schema.model_dump())
    )
    db_farmer_plan = await session.scalar(query.returning(FarmerPlan))

    return db_farmer_plan


@router.delete('/{farmer_plan_id}')
async def delete(farmer_plan_id: int, session: T_Session):
    db_farmer_plan = session.scalar(
        select(FarmerPlan).where(FarmerPlan.id == farmer_plan_id)
    )

    await session.delete(db_farmer_plan)
    await session.commit()

    return {'message': 'FarmerPlan deleted'}
