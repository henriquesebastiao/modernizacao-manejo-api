from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.lote_log import LoteLogRepository
from app.schemas.lote_log import LoteLogCreate, LoteLogSchema, LoteLogUpdate

router = APIRouter(prefix="/lote_log", tags=["LoteLog"])


@router.post("/", response_model=LoteLogSchema, status_code=201)
async def create(cargo: LoteLogCreate, db: AsyncSession = Depends(get_session)):
    repository = LoteLogRepository(db)
    return await repository.create(cargo)


@router.get("/{lote_log_id}", response_model=LoteLogSchema)
async def get_by_id(lote_log_id: int, db: AsyncSession = Depends(get_session)):
    repository = LoteLogRepository(db)
    return await repository.get_by_id(lote_log_id)


@router.get("/", response_model=list[LoteLogSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = LoteLogRepository(db)
    return await repository.get_all()


@router.patch("/{lote_log_id}")
async def update(lote_log_id: int, lote_log: LoteLogUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = LoteLogRepository(db)
    return await repository.update(lote_log_id, lote_log)


@router.delete("/{lote_log_id}")
async def delete(lote_log_id: int, db: AsyncSession = Depends(get_session)):
    repository = LoteLogRepository(db)
    return await repository.delete(lote_log_id)
