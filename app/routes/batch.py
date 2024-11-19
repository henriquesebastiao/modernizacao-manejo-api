from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Batch
from app.schemas import Message
from app.schemas.batch import BatchList, BatchSchema
from app.utils.type import T_Session

router = APIRouter(prefix='/batch', tags=['Batch'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=BatchSchema)
async def create(schema: BatchSchema, session: T_Session):
    db_batch = Batch(**schema.model_dump())

    session.add(db_batch)
    await session.commit()
    await session.refresh(db_batch)

    return db_batch


@router.get('/{batch_id}', response_model=BatchSchema)
async def get_by_id(batch_id: int, session: T_Session):
    db_batch = await session.scalar(select(Batch).where(Batch.id == batch_id))

    return db_batch


@router.get('/', response_model=BatchList)
async def get_all(session: T_Session):
    db_batch = await session.scalars(select(Batch))

    return {'batchs': db_batch.all()}


@router.patch('/{batch_id}', response_model=BatchSchema)
async def update(batch_id: int, schema: BatchSchema, session: T_Session):
    query = up(Batch).where(Batch.id == batch_id).values(**schema.model_dump())

    db_batch = await session.scalar(query.returning(Batch))

    return db_batch


@router.delete('/{batch_id}', response_model=Message)
async def delete(batch_id: int, session: T_Session):
    db_batch = await session.scalar(select(Batch).where(Batch.id == batch_id))

    await session.delete(db_batch)
    await session.commit()

    return {'message': 'Batch deleted'}
