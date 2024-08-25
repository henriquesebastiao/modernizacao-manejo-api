from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy import select

from app.models import User
from app.schemas import Message
from app.schemas.user import UserCreate, UserList, UserSchema, UserUpdate
from app.security import (
    get_current_active_user,
    get_current_user,
    get_password_hash,
)
from app.utils import T_Session

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/', response_model=UserSchema, status_code=HTTPStatus.CREATED)
async def create(schema: UserCreate, session: T_Session):
    db_user = await session.scalar(
        select(User).where(User.email == schema.email)
    )

    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Email already exists'
        )

    schema.password = get_password_hash(schema.password)
    db_user = User(**schema.model_dump())

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.get('/{user_id}', response_model=UserSchema)
async def get_user_by_id(user_id: int, session: T_Session):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User does not exist'
        )

    return db_user


@router.get('/', response_model=UserList)
async def get_all_users(session: T_Session):
    db_users = await session.scalars(select(User))

    return {'users': db_users.all()}


@router.patch('/{user_id}', response_model=UserSchema)
async def update(user_id: int, schema: UserUpdate, session: T_Session):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User does not exist'
        )

    if schema.email:
        db_email_exist = await session.scalar(
            select(User).where(User.email == schema.email)
        )

        if db_email_exist:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, detail='Email already exists'
            )

    if schema.password:
        schema.password = get_password_hash(schema.password)

    for key, value in schema.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.delete('/{user_id}', response_model=Message)
async def delete(user_id: int, session: T_Session):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User does not exist'
        )

    await session.delete(db_user)
    await session.commit()

    return {'message': 'User deleted'}


@router.get('/me', response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)],
):
    return current_user


@router.get('/me/items/')
async def read_own_items(
    current_user: Annotated[
        User, Security(get_current_active_user, scopes=['items'])
    ],
):
    return [{'item_id': 'Foo', 'owner': current_user}]


@router.get('/status/')
async def read_system_status(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return {'status': 'ok'}
