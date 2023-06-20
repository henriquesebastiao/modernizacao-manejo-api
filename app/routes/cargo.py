from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.cargo import CargoRepository
from app.schemas.cargo import CargoCreate, CargoSchema, CargoUpdate

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/")
async def create(cargo: CargoCreate, db: AsyncSession = Depends(get_session)):
    repository = CargoRepository(db)
    return await repository.create(cargo)


@router.get("/{cargo_id}", response_model=CargoSchema)
async def get_by_id(cargo_id: int, db: AsyncSession = Depends(get_session)):
    repository = CargoRepository(db)
    return await repository.get_by_id(cargo_id)


@router.get("/", response_model=list[CargoSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = CargoRepository(db)
    return await repository.get_all()


@router.patch("/{cargo_id}")
async def update(cargo_id: int, cargo: CargoUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = CargoRepository(db)
    return await repository.update(cargo_id, cargo)


@router.delete("/{cargo_id}")
async def delete(cargo_id: int, db: AsyncSession = Depends(get_session)):
    repository = CargoRepository(db)
    return await repository.delete(cargo_id)
