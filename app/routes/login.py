from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.user import User
from app.security import verify_password

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                db: AsyncSession = Depends(get_session)):
    repository = Repository(User, db)
    db_user = await repository.get(form_data.username, "email")
    if not db_user:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")
    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")

    return {"access_token": db_user.email, "token_type": "bearer"}
