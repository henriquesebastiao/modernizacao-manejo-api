from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import AnimalWeight
from app.schemas import Message
from app.schemas.animal import AnimalWeightList, AnimalWeightSchema
from app.utils import T_Session

router = APIRouter(prefix='/animal/weight', tags=['Animal Weight'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=AnimalWeightSchema
)
async def create(schema: AnimalWeightSchema, session: T_Session):
    db_animal_weight = AnimalWeight(**schema.model_dump())

    session.add(db_animal_weight)
    await session.commit()
    await session.refresh(db_animal_weight)

    return db_animal_weight


@router.get('/{animal_weight_id}', response_model=AnimalWeightSchema)
async def get_by_id(animal_weight_id: int, session: T_Session):
    db_animal_weight = await session.scalar(
        select(AnimalWeight).where(AnimalWeight.id == animal_weight_id)
    )

    return db_animal_weight


@router.get('/', response_model=AnimalWeightList)
async def get_all(session: T_Session):
    db_animal_weight = await session.scalars(select(AnimalWeight))

    return {'animal_weights': db_animal_weight.all()}


@router.patch('/{animal_weight_id}', response_model=AnimalWeightSchema)
async def update(
    animal_weight_id: int,
    schema: AnimalWeightSchema,
    session: T_Session,
):
    query = (
        up(AnimalWeight)
        .where(AnimalWeight.id == animal_weight_id)
        .values(**schema.model_dump())
    )

    db_animal_weight = await session.scalar(query.returning(AnimalWeight))

    return db_animal_weight


@router.delete('/{animal_weight_id}', response_model=Message)
async def delete(animal_weight_id: int, session: T_Session):
    db_animal_weight = session.scalar(
        select(AnimalWeight).where(AnimalWeight.id == animal_weight_id)
    )

    await session.delete(db_animal_weight)
    await session.commit()

    return {'message': 'AnimalWeight deleted'}
