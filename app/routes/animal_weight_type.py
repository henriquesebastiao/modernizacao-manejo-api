from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal_weight_type import AnimalWeightType
from app.schemas.animal_weight_type import AnimalWeightTypeSchema

router = APIRouter(prefix="/animal/weight/type",
                   tags=["Animal Weight Type"])


@router.post("/")
async def create(schema: AnimalWeightTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.create(schema)
    await repository.commit()
    return db_animal_weight_type


@router.get("/{animal_weight_type_id}")
async def get_by(animal_weight_type_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.get(animal_weight_type_id)
    return db_animal_weight_type


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.get_all()
    return db_animal_weight_type


@router.patch("/{animal_weight_type_id}")
async def update(animal_weight_type_id: int, user: AnimalWeightTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.update(animal_weight_type_id, user)
    await repository.commit()
    return db_animal_weight_type


@router.delete("/{animal_weight_type_id}")
async def delete(animal_weight_type_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = repository.delete(animal_weight_type_id)
    await repository.commit()
    return db_animal_weight_type
