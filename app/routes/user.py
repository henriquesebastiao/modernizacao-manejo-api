from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import User
from app.schemas import Message
from app.schemas.user import UserCreate, UserList, UserSchema, UserUpdate
from app.security import (
    get_password_hash,
)
from app.utils import T_CurrentUser, T_Session

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/', response_model=UserSchema, status_code=HTTPStatus.CREATED)
async def create_user(schema: UserCreate, session: T_Session):
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
async def get_by_id(user_id: int, session: T_Session):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User does not exist'
        )

    return db_user


@router.get('/', response_model=UserList)
async def get_all(session: T_Session):
    db_users = await session.scalars(select(User))

    return {'users': db_users.all()}


@router.patch('/{user_id}', response_model=UserSchema)
async def update(
    user_id: int,
    schema: UserUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    if user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    db_user = await session.scalar(select(User).where(User.id == user_id))

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
async def delete(
    user_id: int, session: T_Session, current_user: T_CurrentUser
):
    if user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    db_user = await session.scalar(select(User).where(User.id == user_id))

    await session.delete(db_user)
    await session.commit()

    return {'message': 'User deleted'}
