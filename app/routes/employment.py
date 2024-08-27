from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Employment
from app.schemas import Message
from app.schemas.employment import EmploymentList, EmploymentSchema
from app.utils import T_Session

router = APIRouter(prefix='/employment', tags=['Employment'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=EmploymentSchema
)
async def create(schema: EmploymentSchema, session: T_Session):
    db_employment = Employment(**schema.model_dump())

    session.add(db_employment)
    await session.commit()
    await session.refresh(db_employment)

    return db_employment


@router.get('/{employment_id}', response_model=EmploymentSchema)
async def get_by_id(employment_id: int, session: T_Session):
    db_employment = await session.scalar(
        select(Employment).where(Employment.id == employment_id)
    )

    return db_employment


@router.get('/', response_model=EmploymentList)
async def get_all(session: T_Session):
    db_employment = await session.scalars(select(Employment))

    return {'employments': db_employment.all()}


@router.patch('/{employment_id}', response_model=EmploymentSchema)
async def update(
    employment_id: int,
    schema: EmploymentSchema,
    session: T_Session,
):
    query = (
        up(Employment)
        .where(Employment.id == employment_id)
        .values(**schema.model_dump())
    )
    db_employment = await session.scalar(query.returning(Employment))

    return db_employment


@router.delete('/{employment_id}', response_model=Message)
async def delete(employment_id: int, session: T_Session):
    db_employment = await session.scalar(
        select(Employment).where(Employment.id == employment_id)
    )

    await session.delete(db_employment)
    await session.commit()

    return {'message': 'Employment deleted'}
