from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal_weight import AnimalWeight
from app.schemas.animal_weight import AnimalWeightSchema

router = APIRouter(prefix="/animal/weight",
                   tags=["Animal Weight"])


@router.post("/")
async def create(schema: AnimalWeightSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, db)
    await repository.commit()
    db_animal_weight = await repository.create(schema)
    return db_animal_weight


@router.get("/{animal_weight_id}")
async def get_by(animal_weight_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, db)
    db_animal_weight = await repository.get(animal_weight_id)
    return db_animal_weight


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, db)
    db_animal_weight = await repository.get_all()
    return db_animal_weight


@router.patch("/{animal_weight_id}")
async def update(animal_weight_id: int, user: AnimalWeightSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, db)
    await repository.commit()
    db_animal_weight = await repository.update(animal_weight_id, user)
    return db_animal_weight


@router.delete("/{animal_weight_id}")
async def delete(animal_weight_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeight, db)
    db_animal_weight = await repository.delete(animal_weight_id)
    await repository.commit()
    return db_animal_weight
