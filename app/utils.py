from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models import User
from app.security import get_current_user

T_Session = Annotated[AsyncSession, Depends(get_session)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
