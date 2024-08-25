from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models import Breed
from app.schemas.breed import BreedSchema

router = APIRouter(prefix='/animal/breed', tags=['Animal Breed'])


@router.post('/', status_code=HTTPStatus.CREATED)
async def create(schema: BreedSchema, db: AsyncSession = Depends(get_session)):
    """
    Adiciona uma nova raça de animal

    - **name (str)**: Nome da raça
    """
    repository = Repository(Breed, db)
    db_breed = await repository.create(**schema.dict())
    await repository.commit()
    return db_breed


@router.get('/{breed_id}')
async def get_by(breed_id: int, db: AsyncSession = Depends(get_session)):
    """Retorna uma raça de animal pelo seu ID."""
    repository = Repository(Breed, db)
    db_breed = await repository.get(breed_id)
    return db_breed


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todas as raças de animais."""
    repository = Repository(Breed, db)
    db_breed = await repository.get_all()
    return db_breed


@router.patch('/{breed_id}')
async def update(
    breed_id: int, schema: BreedSchema, db: AsyncSession = Depends(get_session)
):
    """
    Atualiza uma raça de animal pelo seu ID.

    - **name (str)**: Nome da raça
    """
    repository = Repository(Breed, db)
    db_breed = await repository.update(breed_id, **schema.dict())
    await repository.commit()
    return db_breed


@router.delete('/{breed_id}')
async def delete(breed_id: int, db: AsyncSession = Depends(get_session)):
    """Deleta uma raça de animal pelo seu ID."""
    repository = Repository(Breed, db)
    db_breed = repository.delete(breed_id)
    await repository.commit()
    return db_breed
