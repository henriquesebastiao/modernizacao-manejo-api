from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import EmploymentPosition
from app.schemas import Message
from app.schemas.employment import (
    EmploymentPositionList,
    EmploymentPositionSchema,
)
from app.utils import T_Session

router = APIRouter(prefix='/employment/position', tags=['Employment Position'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=EmploymentPositionSchema,
)
async def create(schema: EmploymentPositionSchema, session: T_Session):
    db_employment_position = EmploymentPosition(**schema.model_dump())

    session.add(db_employment_position)
    await session.commit()
    await session.refresh(db_employment_position)

    return db_employment_position


@router.get(
    '/{employment_position_id}', response_model=EmploymentPositionSchema
)
async def get_by_id(employment_position_id: int, session: T_Session):
    db_employment_position = session.scalar(
        select(EmploymentPosition).where(
            EmploymentPosition.id == employment_position_id
        )
    )

    return db_employment_position


@router.get('/', response_model=EmploymentPositionList)
async def get_all(session: T_Session):
    db_employment_position = await session.scalars(select(EmploymentPosition))

    return {'employment_positions': db_employment_position.all()}


@router.patch(
    '/{employment_position_id}', response_model=EmploymentPositionSchema
)
async def update(
    employment_position_id: int,
    schema: EmploymentPositionSchema,
    session: T_Session,
):
    query = (
        up(EmploymentPosition)
        .where(EmploymentPosition.id == employment_position_id)
        .values(**schema.model_dump())
    )
    db_employment_position = await session.scalar(
        query.returning(EmploymentPosition)
    )

    return db_employment_position


@router.delete('/{employment_position_id}', response_model=Message)
async def delete(employment_position_id: int, session: T_Session):
    db_employment_position = await session.scalar(
        select(EmploymentPosition).where(
            EmploymentPosition.id == employment_position_id
        )
    )

    await session.delete(db_employment_position)
    await session.commit()

    return {'message': 'EmplomentPosition deleted'}
