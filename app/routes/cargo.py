from fastapi import APIRouter, Depends

from app.schemas.cargo import CargoCreate, CargoSchema, CargoUpdate
from app.services.cargo import CargoService

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/", response_model=CargoSchema, status_code=201)
async def create(cargo: CargoCreate, service=Depends(CargoService)):
    return service.create(cargo)


@router.get("/{cargo_id}", response_model=CargoSchema)
def get_by_id(cargo_id: int, service=Depends(CargoService)):
    return service.get(cargo_id)


@router.get("/", response_model=list[CargoSchema])
async def get_all(service=Depends(CargoService)):
    return service.get_all()


@router.patch("/{cargo_id}")
async def update(cargo_id: int, cargo: CargoUpdate,
                 service=Depends(CargoService)):
    return service.update(cargo_id, cargo)


@router.delete("/{cargo_id}")
async def delete(cargo_id: int, service=Depends(CargoService)) -> dict:
    return service.delete(cargo_id)
