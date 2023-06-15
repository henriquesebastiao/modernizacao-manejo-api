from fastapi import APIRouter, Depends

from app.schemas.login import LoginSchema
from app.services.login import LoginService

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", response_model=LoginSchema, status_code=201)
async def login(user: LoginSchema, service=Depends(LoginService)):
    return service.login(user)

