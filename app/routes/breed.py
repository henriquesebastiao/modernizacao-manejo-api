from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.breed import Breed
from app.schemas.breed import BreedSchema

router = APIRouter(prefix="/animal/breed",
                   tags=["Animal Breed"])


@router.post("/")
async def create(schema: BreedSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    db_breed = await repository.create(schema)
    await repository.commit()
    return db_breed


@router.get("/{breed_id}")
async def get_by(breed_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    db_breed = await repository.get(breed_id)
    return db_breed


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    db_breed = await repository.get_all()
    return db_breed


@router.patch("/{breed_id}")
async def update(breed_id: int, user: BreedSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    db_breed = await repository.update(breed_id, user)
    await repository.commit()
    return db_breed


@router.delete("/{breed_id}")
async def delete(breed_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    db_breed = repository.delete(breed_id)
    await repository.commit()
    return db_breed
