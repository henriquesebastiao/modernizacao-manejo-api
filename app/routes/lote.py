from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.lote import LoteRepository
from app.schemas.lote import LoteCreate, LoteSchema, LoteUpdate

router = APIRouter(prefix="/lote", tags=["Lote"])


@router.post("/", response_model=LoteSchema, status_code=201)
async def create(lote: LoteCreate, db: AsyncSession = Depends(get_session)):
    repository = LoteRepository(db)
    return await repository.create(lote)


@router.get("/{lote_id}", response_model=LoteSchema)
async def get_by_id(lote_id: int, db: AsyncSession = Depends(get_session)):
    repository = LoteRepository(db)
    return await repository.get_by_id(lote_id)


@router.get("/", response_model=list[LoteSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = LoteRepository(db)
    return await repository.get_all()


@router.patch("/{lote_id}")
async def update(lote_id: int, lote: LoteUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = LoteRepository(db)
    return await repository.update(lote_id, lote)


@router.delete("/{lote_id}")
async def delete(lote_id: int, db: AsyncSession = Depends(get_session)):
    repository = LoteRepository(db)
    return await repository.delete(lote_id)
