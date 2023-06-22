from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal_weight_type import AnimalWeightType
from app.schemas.animal_weight_type import AnimalWeightTypeSchema

router = APIRouter(prefix="/animal/weight/type",
                   tags=["Animal Weight Type"])


@router.post("/")
async def create(user: AnimalWeightTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, AnimalWeightTypeSchema, db)
    return await repository.create(user)


@router.get("/{animal_weight_type_id}")
async def get_by_id(animal_weight_type_id: int,
                    db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, AnimalWeightTypeSchema, db)
    return await repository.get(animal_weight_type_id)


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, AnimalWeightTypeSchema, db)
    return await repository.get_all()


@router.patch("/{animal_weight_type_id}")
async def update(animal_weight_type_id: int, user: AnimalWeightTypeSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, AnimalWeightTypeSchema, db)
    return await repository.update(animal_weight_type_id, user)


@router.delete("/{animal_weight_type_id}")
async def delete(animal_weight_type_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(AnimalWeightType, AnimalWeightTypeSchema, db)
    return repository.delete(animal_weight_type_id)
