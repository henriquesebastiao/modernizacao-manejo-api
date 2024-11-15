from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import AnimalWeight
from app.schemas import Message
from app.schemas.animal import (
    AnimalWeightCreate,
    AnimalWeightList,
    AnimalWeightResponse,
    AnimalWeightUpdate,
)
from app.utils.routes import T_CurrentUser, T_Session, upattr

router = APIRouter(prefix='/animal/weight', tags=['Animal Weight'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=AnimalWeightResponse
)
async def create(
    schema: AnimalWeightCreate, session: T_Session, current_user: T_CurrentUser
):
    db_animal_weight = AnimalWeight(**schema.model_dump())

    session.add(db_animal_weight)
    await session.commit()
    await session.refresh(db_animal_weight)

    return db_animal_weight


@router.get('/{animal_weight_id}', response_model=AnimalWeightResponse)
async def get_by_id(
    animal_weight_id: int, session: T_Session, current_user: T_CurrentUser
):
    db_animal_weight = await session.scalar(
        select(AnimalWeight).where(AnimalWeight.id == animal_weight_id)
    )

    if not db_animal_weight:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Weight not exists'
        )

    return db_animal_weight


@router.get('/', response_model=AnimalWeightList)
async def get_all(session: T_Session, current_user: T_CurrentUser):
    db_animal_weight = await session.scalars(select(AnimalWeight))

    return {'animal_weights': db_animal_weight.all()}


@router.patch('/{animal_weight_id}', response_model=AnimalWeightResponse)
async def update(
    animal_weight_id: int,
    schema: AnimalWeightUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal_weight = await session.scalar(
        select(AnimalWeight).where(AnimalWeight.id == animal_weight_id)
    )

    if not db_animal_weight:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Weight not exists'
        )

    upattr(schema, db_animal_weight)

    session.add(db_animal_weight)
    await session.commit()
    await session.refresh(db_animal_weight)

    return db_animal_weight


@router.delete('/{animal_weight_id}', response_model=Message)
async def delete(
    animal_weight_id: int, session: T_Session, current_user: T_CurrentUser
):
    db_animal_weight = await session.scalar(
        select(AnimalWeight).where(AnimalWeight.id == animal_weight_id)
    )

    if not db_animal_weight:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Weight not exists'
        )

    await session.delete(db_animal_weight)
    await session.commit()

    return {'message': 'AnimalWeight deleted'}
