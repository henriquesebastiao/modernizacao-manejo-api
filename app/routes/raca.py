from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.raca import RacaCreate, RacaSchema, RacaUpdate
from app.repositories.raca import RacaRepository

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/", status_code=201)
async def create(cargo: RacaCreate, db: AsyncSession = Depends(get_session)):
    repository = RacaRepository(db)
    return await repository.create(cargo)


@router.get("/{raca_id}", response_model=RacaSchema)
async def get_by_id(raca_id: int, db: AsyncSession = Depends(get_session)):
    repository = RacaRepository(db)
    return await repository.get_by_id(raca_id)


@router.get("/", response_model=list[RacaSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = RacaRepository(db)
    return await repository.get_all()


@router.patch("/{raca_id}")
async def update(raca_id: int, raca: RacaUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = RacaRepository(db)
    return await repository.update(raca_id, raca)


@router.delete("/{raca_id}")
async def delete(raca_id: int, db: AsyncSession = Depends(get_session)):
    repository = RacaRepository(db)
    return await repository.delete(raca_id)
