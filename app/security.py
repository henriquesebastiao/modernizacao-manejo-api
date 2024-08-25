from datetime import datetime, timedelta
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import ExpiredSignatureError, PyJWTError
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session
from zoneinfo import ZoneInfo

from app.database import get_session
from app.models import User
from app.schemas.token import TokenData
from app.settings import Settings

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
settings = Settings()

credentials_exception = HTTPException(
    status_code=HTTPStatus.UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('America/Sao_Paulo')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )

    return encoded_jwt


async def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
):
    expired_token_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Your token has expired',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

        email: str = payload.get('sub')

        if not email:
            raise credentials_exception
        token_data = TokenData(username=email)

    except ExpiredSignatureError:
        raise expired_token_exception
    except PyJWTError:
        raise credentials_exception

    user_db = await session.scalar(
        select(User).where(User.email == token_data.username)
    )

    if not user_db:
        raise credentials_exception

    return user_db


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
