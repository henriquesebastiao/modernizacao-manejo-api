from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import AnimalWeightType
from app.schemas import Message
from app.schemas.animal import AnimalWeightTypeList, AnimalWeightTypeSchema
from app.utils import T_Session

router = APIRouter(prefix='/animal/weight/type', tags=['Animal Weight Type'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=AnimalWeightTypeSchema
)
async def create(schema: AnimalWeightTypeSchema, session: T_Session):
    db_animal_weight_type = AnimalWeightType(**schema.model_dump())

    session.add(db_animal_weight_type)
    await session.commit()
    await session.refresh(db_animal_weight_type)

    return db_animal_weight_type


@router.get('/{animal_weight_type_id}', response_model=AnimalWeightTypeSchema)
async def get_by_id(animal_weight_type_id: int, session: T_Session):
    db_animal_weight_type = await session.scalar(
        select(AnimalWeightType).where(
            AnimalWeightType.id == animal_weight_type_id
        )
    )

    return db_animal_weight_type


@router.get('/', response_model=AnimalWeightTypeList)
async def get_all(session: T_Session):
    db_animal_weight_type = await session.scalars(select(AnimalWeightType))

    return {'db_animal_weight_types': db_animal_weight_type.all()}


@router.patch('/{animal_weight_type_id}', response_model=AnimalWeightType)
async def update(
    animal_weight_type_id: int,
    schema: AnimalWeightTypeSchema,
    session: T_Session,
):
    query = (
        up(AnimalWeightType)
        .where(AnimalWeightType.id == animal_weight_type_id)
        .values(**schema.model_dump())
    )

    db_animal_weight_type = await session.scalar(
        query.returning(AnimalWeightType)
    )

    return db_animal_weight_type


@router.delete('/{animal_weight_type_id}', response_model=Message)
async def delete(animal_weight_type_id: int, session: T_Session):
    db_animal_weight_type = await session.scalar(
        select(AnimalWeightType).where(
            AnimalWeightType.id == animal_weight_type_id
        )
    )

    await session.delete(db_animal_weight_type)
    await session.commit()

    return {'message': 'AnimalWeightType deleted'}
