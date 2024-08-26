from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models import Animal
from app.schemas.animal import AnimalCreate, AnimalSchema, AnimalUpdate
from app.security import get_current_user

router = APIRouter(prefix='/animal', tags=['Animal'])


class Message(BaseModel):
    detail: str


@router.post(
    '/',
    response_model=AnimalSchema,
    status_code=HTTPStatus.CREATED,
    responses={
        HTTPStatus.NOT_FOUND: {
            'model': Message,
            'description': 'Animal not exists',
            'example': {'detail': 'Animal already exists'},
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': Message,
            'description': 'Internal Server Error',
        },
    },
)
async def create(
    schema: AnimalCreate,
    db: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    repository = Repository(Animal, db)
    animal = AnimalSchema(**schema.dict())
    if await repository.get(schema.tag, 'tag'):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Animal already exists'
        )
    elif schema.mother_tag == schema.father_tag:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Mother and Father are the same',
        )
    if mother := await repository.get(schema.mother_tag, 'tag'):
        animal.mother_id = mother.id
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Mother not exists'
        )
    if father := await repository.get(schema.father_tag, 'tag'):
        animal.father_id = father.id
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Father not exists'
        )

    try:
        db_animal = await repository.create(**animal.dict())
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e)
        )
    await repository.commit()
    return db_animal


@router.get('/{animal_id}')
async def get_by_id(
    animal_id: int,
    db: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    repository = Repository(Animal, db)
    db_animal = await repository.get(animal_id)
    return db_animal


@router.get('/')
async def get_all(
    db: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    repository = Repository(Animal, db)
    db_animal = await repository.get_all()
    return db_animal


@router.patch('/{animal_id}')
async def update(
    animal_id: int,
    schema: AnimalUpdate,
    db: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    repository = Repository(Animal, db)
    db_animal = await repository.update(animal_id, **schema.dict())
    await repository.commit()
    return db_animal


@router.delete('/{animal_id}')
async def delete(
    animal_id: int,
    db: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    repository = Repository(Animal, db)
    db_animal = await repository.delete(animal_id)
    await repository.commit()
    return db_animal
