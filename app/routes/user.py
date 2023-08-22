from typing import Annotated

from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserSchema, UserUpdate
from app.security import (
    get_current_active_user,
    get_current_user,
    get_password_hash,
)

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/', response_model=UserSchema, status_code=201)
async def create(schema: UserCreate, db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    schema.password = get_password_hash(schema.password)
    db_user = await repository.create(**schema.dict(), user_type_id=2)
    await repository.commit()
    return db_user


@router.get('/{user_id}')
async def get_by(user_id: int, db: AsyncSession = Depends(get_session)):
    """
    Registra um usuário no banco de dados

    - **first_name (str)**: Nome do usuário
    - **last_name (str)**: Sobrenome do usuário
    - **phone (str)**: Telefone do usuário
    - **email (str)**: Email do usuário
    - **password (str)**: Senha do usuário
    - **create_at (datetime)**: Data de criação do usuário
    - **update_at (datetime)**: Data de atualização do usuário
    - **active (bool)**: Status do usuário
    - **user_type_id (int)**: Tipo de usuário
    - **manager_id (int)**: ID do gerente do usuário
    """
    repository = Repository(User, db)
    db_user = await repository.get(user_id)
    return db_user


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todos os usuários cadastrados no banco de dados."""
    repository = Repository(User, db)
    db_user = await repository.get_all()
    return db_user


@router.patch('/{user_id}')
async def update(
    user_id: int, schema: UserUpdate, db: AsyncSession = Depends(get_session)
):
    """
    Atualiza um usuário no banco de dados

    - **first_name (str)**: Nome do usuário
    - **last_name (str)**: Sobrenome do usuário
    - **email (str)**: Email do usuário
    - **phone (str)**: Telefone do usuário
    - **password (str)**: Senha do usuário
    - **active (bool)**: Status do usuário
    """
    repository = Repository(User, db)
    db_user = await repository.update(user_id, **schema.dict())
    await repository.commit()
    return db_user


@router.delete('/{user_id}')
async def delete(user_id: int, db: AsyncSession = Depends(get_session)):
    """Deleta um usuário do banco de dados."""
    repository = Repository(User, db)
    db_user = repository.delete(user_id)
    await repository.commit()
    return db_user


@router.get('/me', response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)]
):
    return current_user


@router.get('/me/items/')
async def read_own_items(
    current_user: Annotated[
        User, Security(get_current_active_user, scopes=['items'])
    ]
):
    return [{'item_id': 'Foo', 'owner': current_user}]


@router.get('/status/')
async def read_system_status(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {'status': 'ok'}
