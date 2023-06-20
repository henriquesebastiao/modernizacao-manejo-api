from fastapi import APIRouter, Depends

from app.database import get_session
from app.schemas.user import UserCreate, UserUpdate
from app.services.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=201)
async def create(cargo: UserCreate, session=Depends(get_session)):
    service = UserService(session)
    return await service.create(cargo)


@router.get("/{user_id}")
async def get_by_id(user_id: int, session=Depends(get_session)):
    service = UserService(session)
    return await service.get_by_id(user_id)


@router.get("/")
async def get_all(session=Depends(get_session)):
    service = UserService(session)
    return await service.get_all()


@router.patch("/{user_id}")
async def update(user_id: int, user: UserUpdate,
                 session=Depends(get_session)):
    service = UserService(session)
    return await service.update(user_id, user)


@router.delete("/{user_id}")
async def delete(user_id: int, service=Depends(UserService)) -> dict:
    return service.delete(user_id)
