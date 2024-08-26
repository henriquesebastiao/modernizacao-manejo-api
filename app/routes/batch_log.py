from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models import BatchLog
from app.schemas.batch import BatchLogSchema

router = APIRouter(prefix='/animal/batch_log', tags=['Animal Batch Log'])


@router.post('/', status_code=HTTPStatus.CREATED)
async def create(
    schema: BatchLogSchema, db: AsyncSession = Depends(get_session)
):
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.create(**schema.dict())
    await repository.commit()
    return db_batch_log


@router.get('/{batch_log_id}')
async def get_by_id(
    batch_log_id: int, db: AsyncSession = Depends(get_session)
):
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.get(batch_log_id)
    return db_batch_log


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.get_all()
    return db_batch_log


@router.patch('/{batch_log_id}')
async def update(
    batch_log_id: int,
    schema: BatchLogSchema,
    db: AsyncSession = Depends(get_session),
):
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.update(batch_log_id, **schema.dict())
    await repository.commit()
    return db_batch_log


@router.delete('/{batch_log_id}')
async def delete(batch_log_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, db)
    db_batch_log = repository.delete(batch_log_id)
    await repository.commit()
    return db_batch_log
