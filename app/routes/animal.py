from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal import Animal
from app.schemas.animal import AnimalSchema

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/")
async def create(schema: AnimalSchema, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = await repository.create(schema)
    await repository.commit()
    return db_animal


@router.get("/{animal_id}")
async def get_by(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = repository.get(animal_id)
    return db_animal


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = repository.get_all()
    return db_animal


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = repository.update(animal_id, animal)
    await repository.commit()
    return db_animal


@router.delete("/{animal_id}")
async def delete(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = repository.delete(animal_id)
    await repository.commit()
    return db_animal
