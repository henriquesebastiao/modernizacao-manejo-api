from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal import AnimalWeightType
from app.schemas.animal_weight_type import AnimalWeightTypeSchema

router = APIRouter(prefix='/animal/weight/type', tags=['Animal Weight Type'])


@router.post('/', status_code=201)
async def create(
    schema: AnimalWeightTypeSchema, db: AsyncSession = Depends(get_session)
):
    """
    Adiciona um novo tipo de peso de animal.

    - **name (str)**: Nome do tipo de peso de animal.
    """
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.create(**schema.dict())
    await repository.commit()
    return db_animal_weight_type


@router.get('/{animal_weight_type_id}')
async def get_by(
    animal_weight_type_id: int, db: AsyncSession = Depends(get_session)
):
    """Retorna um tipo de peso de animal pelo seu ID."""
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.get(animal_weight_type_id)
    return db_animal_weight_type


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todos os tipos de peso de animal."""
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.get_all()
    return db_animal_weight_type


@router.patch('/{animal_weight_type_id}')
async def update(
    animal_weight_type_id: int,
    schema: AnimalWeightTypeSchema,
    db: AsyncSession = Depends(get_session),
):
    """
    Atualiza um tipo de peso de animal com base no seu ID.

    - **name (str)**: Nome do tipo de peso de animal.
    """
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = await repository.update(
        animal_weight_type_id, **schema.dict()
    )
    await repository.commit()
    return db_animal_weight_type


@router.delete('/{animal_weight_type_id}')
async def delete(
    animal_weight_type_id: int, db: AsyncSession = Depends(get_session)
):
    """Deleta um tipo de peso de animal com base no seu ID."""
    repository = Repository(AnimalWeightType, db)
    db_animal_weight_type = repository.delete(animal_weight_type_id)
    await repository.commit()
    return db_animal_weight_type
