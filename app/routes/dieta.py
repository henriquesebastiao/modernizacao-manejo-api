from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.dieta import DietaRepository
from app.schemas.dieta import DietaCreate, DietaSchema, DietaUpdate

router = APIRouter(prefix="/dieta", tags=["Dieta"])


@router.post("/", response_model=DietaSchema, status_code=201)
async def create(cargo: DietaCreate, db: AsyncSession = Depends(get_session)):
    repository = DietaRepository(db)
    return await repository.create(cargo)


@router.get("/{dieta_id}", response_model=DietaSchema)
async def get_by_id(dieta_id: int, db: AsyncSession = Depends(get_session)):
    repository = DietaRepository(db)
    return await repository.get_by_id(dieta_id)


@router.get("/", response_model=list[DietaSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = DietaRepository(db)
    return await repository.get_all()


@router.patch("/{dieta_id}")
async def update(dieta_id: int, dieta: DietaUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = DietaRepository(db)
    return await repository.update(dieta_id, dieta)


@router.delete("/{dieta_id}")
async def delete(dieta_id: int, db: AsyncSession = Depends(get_session)):
    repository = DietaRepository(db)
    return await repository.delete(dieta_id)
