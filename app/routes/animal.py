from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.animal import AnimalRepository
from app.schemas.animal import AnimalCreate, AnimalUpdate

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/")
async def create(cargo: AnimalCreate, db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.create(cargo)


@router.get("/{animal_id}")
async def get_by_id(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.get_by_id(animal_id)


@router.get("/{brinco}")
async def get_by_brinco(brinco: str, db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.get_by_field("brinco", brinco)


@router.get("/{chip}")
async def get_by_chip(chip: str, db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.get_by_field("chip", chip)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.get_all()


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.update(animal_id, animal)


@router.delete("/{animal_id}")
async def delete(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = AnimalRepository(db)
    return await repository.delete(animal_id)
