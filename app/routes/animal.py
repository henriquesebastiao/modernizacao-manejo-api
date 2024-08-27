from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Animal
from app.schemas.animal import (
    AnimalCreate,
    AnimalList,
    AnimalSchema,
    AnimalUpdate,
)
from app.utils import T_CurrentUser, T_Session

router = APIRouter(prefix='/animal', tags=['Animal'])


@router.post(
    '/',
    response_model=AnimalSchema,
    status_code=HTTPStatus.CREATED,
)
async def create(
    schema: AnimalCreate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = Animal(**schema.model_dump())

    session.add(db_animal)
    await session.commit()
    await session.refresh(db_animal)

    return db_animal


@router.get('/{animal_id}', response_model=AnimalSchema)
async def get_by_id(
    animal_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalar(
        select(Animal).where(Animal.id == animal_id)
    )

    return db_animal


@router.get('/', response_model=AnimalList)
async def get_all(
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalars(select(Animal))

    return {'animals': db_animal.all()}


@router.patch('/{animal_id}', response_model=AnimalSchema)
async def update(
    animal_id: int,
    schema: AnimalUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    query = (
        up(Animal).where(Animal.id == animal_id).values(**schema.model_dump())
    )

    db_animal = await session.scalar(query.returning(Animal))

    return db_animal


@router.delete('/{animal_id}')
async def delete(
    animal_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalar(
        select(Animal).where(Animal.id == animal_id)
    )

    await session.delete(db_animal)
    await session.commit()

    return {'message': 'Animal deleted'}
