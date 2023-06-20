from fastapi import APIRouter, Depends

from app.database import get_session
from app.schemas.login import LoginSchema
from app.services.login import LoginService

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", status_code=201)
async def login(user: LoginSchema, session=Depends(get_session)):
    service = LoginService(session)
    return await service.login(user)

