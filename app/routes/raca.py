from fastapi import APIRouter, Depends

from app.schemas.raca import RacaCreate, RacaSchema, RacaUpdate
from app.services.raca import RacaService

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/", response_model=RacaSchema, status_code=201)
async def create(cargo: RacaCreate, service=Depends(RacaService)):
    return service.create(cargo)


@router.get("/{raca_id}", response_model=RacaSchema)
def get_by_id(raca_id: int, service=Depends(RacaService)):
    return service.get_by_id(raca_id)


@router.get("/", response_model=list[RacaSchema])
async def get_all(service=Depends(RacaService)):
    return service.get_all()


@router.patch("/{raca_id}")
async def update(raca_id: int, raca: RacaUpdate,
                 service=Depends(RacaService)):
    return service.update(raca_id, raca)


@router.delete("/{raca_id}")
async def delete(raca_id: int, service=Depends(RacaService)) -> dict:
    return service.delete(raca_id)
