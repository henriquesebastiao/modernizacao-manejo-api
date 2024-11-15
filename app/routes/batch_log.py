from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import BatchLog
from app.schemas import Message
from app.schemas.batch import BatchLogList, BatchLogSchema
from app.utils import T_Session

router = APIRouter(prefix='/batch/log', tags=['Batch Log'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=BatchLogSchema
)
async def create(schema: BatchLogSchema, session: T_Session):
    db_batch_log = BatchLog(**schema.model_dump())

    session.add(db_batch_log)
    await session.commit()
    session.refresh(db_batch_log)

    return db_batch_log


@router.get('/{batch_log_id}', response_model=BatchLogSchema)
async def get_by_id(batch_log_id: int, session: T_Session):
    db_batch_log = await session.scalar(
        select(BatchLog).where(BatchLog.id == batch_log_id)
    )

    return db_batch_log


@router.get('/', response_model=BatchLogList)
async def get_all(session: T_Session):
    db_batch_log = await session.scalars(select(BatchLog))

    return {'batch_logs': db_batch_log.all()}


@router.patch('/{batch_log_id}', response_model=BatchLogSchema)
async def update(
    batch_log_id: int,
    schema: BatchLogSchema,
    session: T_Session,
):
    query = (
        up(BatchLog)
        .where(BatchLog.id == batch_log_id)
        .values(**schema.model_dump())
    )

    db_batch_log = await session.scalar(query.returning(BatchLog))

    return db_batch_log


@router.delete('/{batch_log_id}', response_model=Message)
async def delete(batch_log_id: int, session: T_Session):
    db_batch_log = await session.scalar(
        select(BatchLog).where(BatchLog.id == batch_log_id)
    )

    await session.delete(db_batch_log)
    await session.commit()

    return {'message': 'BatchLog deleted'}
