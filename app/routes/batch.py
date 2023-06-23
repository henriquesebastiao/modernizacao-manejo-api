from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.batch import Batch
from app.schemas.batch import BatchSchema

router = APIRouter(prefix="/animal/batch",
                   tags=["Animal batch"])


@router.post("/")
async def create(schema: BatchSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, db)
    db_batch = await repository.create(**schema.dict())
    await repository.commit()
    return db_batch


@router.get("/{batch_id}")
async def get_by(batch_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, db)
    db_batch = await repository.get(batch_id)
    await repository.commit()
    return db_batch


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, db)
    db_batch = await repository.get_all()
    return db_batch


@router.patch("/{batch_id}")
async def update(batch_id: int, user: BatchSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, db)
    db_batch = await repository.update(batch_id, user)
    return db_batch


@router.delete("/{batch_id}")
async def delete(batch_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Batch, db)
    db_batch = repository.delete(batch_id)
    await repository.commit()
    return db_batch
