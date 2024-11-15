from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Farm
from app.schemas import Message
from app.schemas.farm import FarmList, FarmSchema
from app.utils.routes import T_Session

router = APIRouter(prefix='/farm', tags=['Farm'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=FarmSchema)
async def create(schema: FarmSchema, session: T_Session):
    db_farm = Farm(**schema.model_dump())

    session.add(db_farm)
    await session.commit()
    await session.refresh(db_farm)

    return db_farm


@router.get('/{farm_id}', response_model=FarmSchema)
async def get_by_id(farm_id: int, session: T_Session):
    db_farm = await session.scalar(select(Farm).where(Farm.id == farm_id))

    return db_farm


@router.get('/', response_model=FarmList)
async def get_all(session: T_Session):
    db_farm = await session.scalars(select(Farm))

    return {'farms': db_farm.all()}


@router.patch('/{farm_id}', response_model=FarmSchema)
async def update(farm_id: int, schema: FarmSchema, session: T_Session):
    query = up(Farm).where(Farm.id == farm_id).values(**schema.model_dump())
    db_farm = await session.scalar(query.returning(Farm))

    return db_farm


@router.delete('/{farm_id}', response_model=Message)
async def delete(farm_id: int, session: T_Session):
    db_farm = await session.scalar(select(Farm).where(Farm.id == farm_id))

    await session.delete(db_farm)
    await session.commit()

    return {'message': 'Farm deleted'}
