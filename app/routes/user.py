from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate, UserSchema, UserUpdate
from app.services.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=UserSchema, status_code=201)
async def create(cargo: UserCreate, service=Depends(UserService)):
    return service.create(cargo)


@router.get("/{user_id}", response_model=UserSchema)
def get_by_id(user_id: int, service=Depends(UserService)):
    return service.get_by_id(user_id)


@router.get("/", response_model=list[UserSchema])
async def get_all(service=Depends(UserService)):
    return service.get_all()


@router.patch("/{user_id}")
async def update(user_id: int, user: UserUpdate,
                 service=Depends(UserService)):
    return service.update(user_id, user)


@router.delete("/{user_id}")
async def delete(user_id: int, service=Depends(UserService)) -> dict:
    return service.delete(user_id)
