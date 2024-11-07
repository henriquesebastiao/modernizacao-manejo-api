from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Animal
from app.schemas.animal import (
    AnimalCreate,
    AnimalList,
    AnimalSchema,
    AnimalUpdate,
)
from app.utils import T_CurrentUser, T_Session, upattr

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
    db_animal = await session.scalar(
        select(Animal).where(Animal.tag == schema.tag)
    )

    if db_animal:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Animal already exists'
        )

    db_animal = Animal(**schema.model_dump())

    session.add(db_animal)
    await session.commit()
    await session.refresh(db_animal)

    return db_animal


@router.get('/{tag}', response_model=AnimalSchema)
async def get_by_id(
    tag: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalar(
        select(Animal).where(Animal.tag == tag)
    )

    if not db_animal:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Animal does not exist'
        )

    return db_animal


@router.get('/', response_model=AnimalList)
async def get_all(
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalars(select(Animal))

    return {'animals': db_animal.all()}


@router.patch('/{tag}', response_model=AnimalSchema)
async def update(
    tag: int,
    schema: AnimalUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalar(select(Animal).where(Animal.tag == tag))

    if not db_animal:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Animal does not exist'
        )

    upattr(schema, db_animal)

    session.add(db_animal)
    await session.commit()
    await session.refresh(db_animal)
    return db_animal


@router.delete('/{tag}')
async def delete(
    tag: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_animal = await session.scalar(
        select(Animal).where(Animal.tag == tag)
    )

    if not db_animal:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Animal does not exist'
        )

    await session.delete(db_animal)
    await session.commit()

    return {'message': 'Animal deleted'}
