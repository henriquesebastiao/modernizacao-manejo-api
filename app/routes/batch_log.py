from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.batch_log import BatchLog
from app.schemas.batch_log import BatchLogSchema

router = APIRouter(prefix="/animal/batch_log",
                   tags=["Animal Batch Log"])


@router.post("/")
async def create(user: BatchLogSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, BatchLogSchema, db)
    return await repository.create(user)


@router.get("/{batch_log_id}")
async def get_by(batch_log_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, BatchLogSchema, db)
    return await repository.get(batch_log_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, BatchLogSchema, db)
    return await repository.get_all()


@router.patch("/{batch_log_id}")
async def update(batch_log_id: int, user: BatchLogSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, BatchLogSchema, db)
    return await repository.update(batch_log_id, user)


@router.delete("/{batch_log_id}")
async def delete(batch_log_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(BatchLog, BatchLogSchema, db)
    return repository.delete(batch_log_id)
