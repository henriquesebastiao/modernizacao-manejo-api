from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.models import User
from app.schemas.token import Token
from app.security import (
    create_access_token,
    get_current_user,
    verify_password,
)
from app.utils import T_OAuth2Form, T_Session

router = APIRouter(tags=['Token'])


@router.post('/token', response_model=Token)
async def login_for_access_token(
    session: T_Session,
    form_data: T_OAuth2Form,
):
    invalid_credentials_exception = HTTPException(
        status_code=HTTPStatus.BAD_REQUEST,
        detail='Incorrect email or password',
    )

    user = await session.scalar(
        select(User).where(User.email == form_data.username)
    )

    if not user:
        raise invalid_credentials_exception
    elif not verify_password(form_data.password, user.password):
        raise invalid_credentials_exception

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}


@router.post('/refresh_token', response_model=Token)
async def refresh_access_token(user: User = Depends(get_current_user)):
    new_access_token = create_access_token(data={'sub': user.email})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
