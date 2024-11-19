from typing import Annotated, Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic_extra_types.phone_numbers import (
    PhoneNumber,
    PhoneNumberValidator,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.core.security import get_current_user
from app.models import User

T_Session = Annotated[AsyncSession, Depends(get_session)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_PhoneNumberBR = Annotated[
    Union[str, PhoneNumber], PhoneNumberValidator(default_region='BR')
]
