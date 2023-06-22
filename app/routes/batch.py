from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.batch import Batch
from app.schemas.batch import BatchSchema

router = APIRouter(prefix="/animal/weight",
                   tags=["Animal Weight"])


@router.post("/")
async def create(user: BatchSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, BatchSchema, db)
    return await repository.create(user)


@router.get("/{batch_id}")
async def get_by(batch_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, BatchSchema, db)
    return await repository.get(batch_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, BatchSchema, db)
    return await repository.get_all()


@router.patch("/{batch_id}")
async def update(batch_id: int, user: BatchSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, BatchSchema, db)
    return await repository.update(batch_id, user)


@router.delete("/{batch_id}")
async def delete(batch_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, BatchSchema, db)
    return repository.delete(batch_id)
