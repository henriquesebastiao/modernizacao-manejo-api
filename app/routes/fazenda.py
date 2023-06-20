from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.fazenda import FazendaRepository
from app.schemas.fazenda import FazendaCreate, FazendaSchema, FazendaUpdate

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/", response_model=FazendaSchema, status_code=201)
async def create(cargo: FazendaCreate, db: AsyncSession = Depends(get_session)):
    repository = FazendaRepository(db)
    return await repository.create(cargo)


@router.get("/{fazenda_id}", response_model=FazendaSchema)
async def get_by_id(fazenda_id: int, db: AsyncSession = Depends(get_session)):
    repository = FazendaRepository(db)
    return await repository.get_by_id(fazenda_id)


@router.get("/", response_model=list[FazendaSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = FazendaRepository(db)
    return await repository.get_all()


@router.patch("/{fazenda_id}")
async def update(fazenda_id: int, fazenda: FazendaUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = FazendaRepository(db)
    return await repository.update(fazenda_id, fazenda)


@router.delete("/{fazenda_id}")
async def delete(fazenda_id: int, db: AsyncSession = Depends(get_session)):
    repository = FazendaRepository(db)
    return await repository.delete(fazenda_id)
