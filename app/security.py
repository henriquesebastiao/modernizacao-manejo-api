from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import Settings
from app.crud import Repository
from app.database import get_session
from app.models import User
from app.schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

settings = Settings()


def verify_password(plain_password, hashed_password):
    """Verifica se o hash da senha é igual ao hash do banco de dados"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Gera o hash da senha"""
    return pwd_context.hash(password)


async def get_user(db, username: str):
    """Retorna o usuário do banco de dados"""
    db_user = await Repository(User, db).get(username, 'email')
    if db_user:
        return db_user


async def authenticate_user(db, username: str, password: str):
    """Verifica se o usuário existe e se a senha está correta"""
    user = await get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Cria o token de acesso"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_session),
):
    """Retorna o usuário atual"""
    credentials_exception = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get('email')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    """Retorna o usuário atual se ele estiver ativo"""
    return current_user
