from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal_weight import AnimalWeight
from app.schemas.animal_weight import AnimalWeightSchema

router = APIRouter(prefix="/animal/weight",
                   tags=["Animal Weight"])


@router.post("/")
async def create(user: AnimalWeightSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, AnimalWeightSchema, db)
    return await repository.create(user)


@router.get("/{animal_weight_id}")
async def get_by_id(animal_weight_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, AnimalWeightSchema, db)
    return await repository.get(animal_weight_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, AnimalWeightSchema, db)
    return await repository.get_all()


@router.patch("/{animal_weight_id}")
async def update(animal_weight_id: int, user: AnimalWeightSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, AnimalWeightSchema, db)
    return await repository.update(animal_weight_id, user)


@router.delete("/{animal_weight_id}")
async def delete(animal_weight_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, AnimalWeightSchema, db)
    return repository.delete(animal_weight_id)
