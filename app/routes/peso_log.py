from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.peso_log import PesoLogRepository
from app.schemas.peso_log import PesoLogCreate, PesoLogSchema, PesoLogUpdate

router = APIRouter(prefix="/peso_log", tags=["PesoLog"])


@router.post("/")
async def create(peso: PesoLogCreate, db: AsyncSession = Depends(get_session)):
    repository = PesoLogRepository(db)
    return await repository.create(peso)


@router.get("/{peso_log_id}", response_model=PesoLogSchema)
async def get_by_id(peso_log_id: int, db: AsyncSession = Depends(get_session)):
    repository = PesoLogRepository(db)
    return await repository.get_by_id(peso_log_id)


@router.get("/", response_model=list[PesoLogSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = PesoLogRepository(db)
    return await repository.get_all()


@router.patch("/{peso_log_id}")
async def update(peso_log_id: int, peso_log: PesoLogUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = PesoLogRepository(db)
    return await repository.update(peso_log_id, peso_log)


@router.delete("/{peso_log_id}")
async def delete(peso_log_id: int, db: AsyncSession = Depends(get_session)):
    repository = PesoLogRepository(db)
    return await repository.delete(peso_log_id)
