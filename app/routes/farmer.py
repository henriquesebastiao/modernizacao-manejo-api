from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Farmer
from app.schemas import Message
from app.schemas.farmer import (
    FarmerCreate,
    FarmerList,
    FarmerSchema,
    FarmerUpdate,
)
from app.utils import T_CurrentUser, T_Session

router = APIRouter(prefix='/farmer', tags=['Farmer'])


@router.post('/', response_model=FarmerSchema, status_code=HTTPStatus.CREATED)
async def create(
    schema: FarmerCreate, session: T_Session, current_user: T_CurrentUser
):
    if schema.user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    db_farmer = await session.scalar(
        select(Farmer).where(Farmer.user_id == schema.user_id)
    )

    if db_farmer:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='There is already a Farmer for this user',
        )

    db_farmer = Farmer(**schema.model_dump())

    session.add(db_farmer)
    await session.commit()
    await session.refresh(db_farmer)

    return db_farmer


@router.get('/{farmer_id}', response_model=FarmerSchema)
async def get_by_id(farmer_id: int, session: T_Session):
    db_farmer = await session.scalar(
        select(Farmer).where(Farmer.id == farmer_id)
    )

    if not db_farmer:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Farmer does not exist'
        )

    return db_farmer


@router.get('/', response_model=FarmerList)
async def get_all(session: T_Session):
    db_farmer = await session.scalars(select(Farmer))

    return {'farmers': db_farmer.all()}


@router.patch('/{farmer_id}', response_model=FarmerSchema)
async def update(
    farmer_id: int,
    schema: FarmerUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_farmer = await session.scalar(
        select(Farmer).where(Farmer.id == farmer_id)
    )

    if not db_farmer:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Farmer does not exist'
        )
    elif db_farmer.user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    query = (
        up(Farmer).where(Farmer.id == farmer_id).values(**schema.model_dump())
    )
    db_farmer = await session.scalar(query.returning(Farmer))

    return db_farmer


@router.delete('/{farmer_id}', response_model=Message)
async def delete(
    farmer_id: int, session: T_Session, current_user: T_CurrentUser
):
    db_farmer = await session.scalar(
        select(Farmer).where(Farmer.id == farmer_id)
    )

    if not db_farmer:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Farmer does not exist'
        )
    elif db_farmer.user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    await session.delete(db_farmer)
    await session.commit()

    return {'message': 'Farmer deleted'}
