from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy import update as up

from app.models import Breed
from app.schemas import Message
from app.schemas.breed import BreedList, BreedSchema
from app.utils import T_Session

router = APIRouter(prefix='/animal/breed', tags=['Animal Breed'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=BreedSchema)
async def create(schema: BreedSchema, session: T_Session):
    db_breed = Breed(**schema.model_dump())

    session.add(db_breed)
    await session.commit()
    await session.refresh(db_breed)

    return db_breed


@router.get('/{breed_id}', response_model=BreedSchema)
async def get_by_id(breed_id: int, session: T_Session):
    db_breed = await session.scalar(select(Breed).where(Breed.id == breed_id))

    return db_breed


@router.get('/', response_model=BreedList)
async def get_all(session: T_Session):
    db_breed = await session.scalars(select(Breed))

    return {'breeds': db_breed.all()}


@router.patch('/{breed_id}', response_model=BreedSchema)
async def update(breed_id: int, schema: BreedSchema, session: T_Session):
    query = up(Breed).where(Breed.id == breed_id).values(**schema.model_dump())
    db_breed = await session.scalar(query.returning(Breed))

    return db_breed


@router.delete('/{breed_id}', response_model=Message)
async def delete(breed_id: int, session: T_Session):
    db_breed = session.scalar(select(Breed).where(Breed.id == breed_id))

    await session.delete(db_breed)
    await session.commit()

    return {'message': 'Breed deleted'}
