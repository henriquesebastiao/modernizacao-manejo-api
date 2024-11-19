from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.core.security import get_password_hash
from app.models import Employment, User
from app.schemas import Message
from app.schemas.user import (
    SubordinateUserCreate,
    SubordinateUserSchema,
    UserCreate,
    UserList,
    UserSchema,
    UserUpdate,
)
from app.utils import response
from app.utils.db import upattr
from app.utils.enum import EmploymentPositions
from app.utils.message import AlreadyExists, DoesNotExist, NotAuthorized
from app.utils.type import T_CurrentUser, T_Session

router = APIRouter(prefix='/user', tags=['User'])


@router.post(
    '/',
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    responses=response.CREATE_USER,
    summary='Cria um novo usuário',
)
async def create_user(schema: UserCreate, session: T_Session):
    """
    Cadastra um novo usuário na aplicação com as seguintes informações:

    - **first_name**: primeiro nome
    - **last_name**: sobrenome (opcional)
    - **email**: email do usuário a ser cadastrato
    - **password**: senha do usuário
    - **phone**: número de telefone do usuário (opcional)

    ### Respostas

    - `201` - Usuário criado com sucesso.
    - `409` - Erro caso já exista um usuário com o email fornecido.
    - `422` - Erro de validação dos dados.
    """
    db_user = await session.scalar(
        select(User).where(User.email == schema.email)
    )

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=AlreadyExists.EMAIL
        )

    schema.password = get_password_hash(schema.password)
    db_user = User(**schema.model_dump())

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.post(
    '/employee/',
    response_model=SubordinateUserSchema,
    status_code=status.HTTP_201_CREATED,
    responses=response.CREATE_SUBORDINATE_USER,
    summary='Cria um novo usuário subordinado',
)
async def create_subordinate_user(
    schema: SubordinateUserCreate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    """
    Cadastra um usuário subordinado a um fazendeiro.

    Dados:
    - **first_name**: primeiro nome
    - **last_name**: sobrenome (opcional)
    - **email**: email do usuário a ser cadastrato
    - **password**: senha do usuário
    - **phone**: número de telefone do usuário (opcional)
    - **manager_id**: id do fazendo do qual o novo usuário é funcionário.

    ### Respostas

    - `201` Usuário subordinado criado com sucesso.
    - `403` Erro caso o usuário que está tentado cadastrar um usuário
    subordinado não tenha um cargo de Farmer ou Manager, ou o
    - `409` Erro caso já exista um usuário com o email fornecido.
    - `422` Erro de validação dos dados.
    """
    current_user_employment = await session.scalar(
        select(Employment).where(Employment.farmer_id == current_user.id)
    )

    if current_user_employment is None or (
        current_user_employment.employment_position
        not in {EmploymentPositions.FARMER, EmploymentPositions.MANAGER}
    ):
        if (
            not current_user_employment.employment_position
            == EmploymentPositions.MANAGER
            and current_user_employment.farmer_id != schema.manager_id
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=NotAuthorized.REGISTER_EMPLOYEE,
            )

    db_user = await session.scalar(
        select(User).where(User.email == schema.email)
    )

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=AlreadyExists.EMAIL
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
            status_code=status.HTTP_404_NOT_FOUND, detail=DoesNotExist.USER
        )

    return db_user


@router.get(
    '/',
    response_model=UserList,
    deprecated=True,
    summary='Retorna todos os usuários cadastrados',
)
async def get_all(session: T_Session):
    """
    Retorna todos os usuários cadastrados na aplicação.

    Esta rota é deprecada e somente deve ser usada para debugging
    em desenvolvimento, sendo removida para deploy em produção.
    """
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
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Not enough permission',
        )

    db_user = await session.scalar(select(User).where(User.id == user_id))

    if schema.email:
        db_email_exist = await session.scalar(
            select(User).where(User.email == schema.email)
        )

        if db_email_exist:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=AlreadyExists.EMAIL,
            )

    if schema.password:
        schema.password = get_password_hash(schema.password)

    upattr(schema, db_user)

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
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Not enough permission',
        )

    db_user = await session.scalar(select(User).where(User.id == user_id))

    await session.delete(db_user)
    await session.commit()

    return {'message': 'User deleted'}
