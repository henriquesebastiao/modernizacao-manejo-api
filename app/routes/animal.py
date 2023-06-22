from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal import Animal
from app.schemas.animal import AnimalSchema

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/")
async def create(animal: AnimalSchema, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.create(animal)


@router.get("/{animal_id}")
async def get_by_id(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.get(animal_id)


@router.get("/{tag}")
async def get_by_tag(tag: str, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.get("tag", tag)


@router.get("/{sisbov}")
async def get_by_sisbov(sisbov: str, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.get("SISBOV", sisbov)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.get_all()


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.update(animal_id, animal)


@router.delete("/{animal_id}")
async def delete(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    return await repository.delete(animal_id)
