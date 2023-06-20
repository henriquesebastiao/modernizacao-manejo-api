from fastapi import APIRouter, Depends

from app.database import get_session
from app.schemas.cargo import CargoCreate, CargoSchema, CargoUpdate
from app.services.cargo import CargoService

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/")
async def create(cargo: CargoCreate, session=Depends(get_session)):
    service = CargoService(session)
    return await service.create(cargo)


@router.get("/{cargo_id}", response_model=CargoSchema)
async def get_by_id(cargo_id: int, session=Depends(get_session)):
    service = CargoService(session)
    return await service.get_by_id(cargo_id)


@router.get("/", response_model=list[CargoSchema])
async def get_all(session=Depends(get_session)):
    service = CargoService(session)
    return await service.get_all()


@router.patch("/{cargo_id}")
async def update(cargo_id: int, cargo: CargoUpdate,
                 session=Depends(get_session)):
    service = CargoService(session)
    return await service.update(cargo_id, cargo)


@router.delete("/{cargo_id}")
async def delete(cargo_id: int, session=Depends(get_session)) -> dict:
    service = CargoService(session)
    return await service.delete(cargo_id)
