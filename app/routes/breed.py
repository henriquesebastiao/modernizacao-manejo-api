from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.breed import Breed
from app.schemas.breed import BreedSchema

router = APIRouter(prefix="/animal/breed",
                   tags=["Animal Breed"])


@router.post("/")
async def create(user: BreedSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    return await repository.create(user)


@router.get("/{breed_id}")
async def get_by(breed_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    return await repository.get(breed_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    return await repository.get_all()


@router.patch("/{breed_id}")
async def update(breed_id: int, user: BreedSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    return await repository.update(breed_id, user)


@router.delete("/{breed_id}")
async def delete(breed_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Breed, BreedSchema, db)
    return repository.delete(breed_id)
