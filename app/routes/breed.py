from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Breed
from app.schemas import Message
from app.schemas.breed import BreedCreateUpdate, BreedList, BreedSchema
from app.utils import T_CurrentUser, T_Session

router = APIRouter(prefix='/animal/breed', tags=['Animal Breed'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=BreedSchema)
async def create(
    schema: BreedCreateUpdate, session: T_Session, current_user: T_CurrentUser
):
    db_breed = await session.scalar(
        select(Breed).where(Breed.name == schema.name)
    )

    if db_breed:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Breed already exists'
        )

    db_breed = Breed(**schema.model_dump())

    session.add(db_breed)
    await session.commit()
    await session.refresh(db_breed)

    return db_breed


@router.get('/', response_model=BreedList)
async def get_all(session: T_Session, current_user: T_CurrentUser):
    db_breed = await session.scalars(select(Breed))

    return {'breeds': db_breed.all()}


@router.patch('/{name}', response_model=BreedSchema)
async def update(
    name: str,
    schema: BreedCreateUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_breed = await session.scalar(select(Breed).where(Breed.name == name))

    if not db_breed:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Breed not found'
        )

    db_breed.name = schema.name

    session.add(db_breed)
    await session.commit()
    await session.refresh(db_breed)
    return db_breed


@router.delete('/{name}', response_model=Message)
async def delete(name: str, session: T_Session, current_user: T_CurrentUser):
    db_breed = await session.scalar(select(Breed).where(Breed.name == name))

    if not db_breed:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Breed not found'
        )

    await session.delete(db_breed)
    await session.commit()

    return {'message': 'Breed deleted'}
