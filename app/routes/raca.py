from fastapi import APIRouter, Depends

from app.database import get_session
from app.schemas.raca import RacaCreate, RacaSchema, RacaUpdate
from app.services.raca import RacaService

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/", status_code=201)
async def create(cargo: RacaCreate, session=Depends(get_session)):
    service = RacaService(session)
    return await service.create(cargo)


@router.get("/{raca_id}")
async def get_by_id(raca_id: int, session=Depends(get_session)):
    service = RacaService(session)
    return await service.get_by_id(raca_id)


@router.get("/", response_model=list[RacaSchema])
async def get_all(session=Depends(get_session)):
    service = RacaService(session)
    return await service.get_all()


@router.patch("/{raca_id}")
async def update(raca_id: int, raca: RacaUpdate,
                 service=Depends(RacaService)):
    return await service.update(raca_id, raca)


@router.delete("/{raca_id}")
async def delete(raca_id: int, session=Depends(get_session)) -> dict:
    service = RacaService(session)
    return await service.delete(raca_id)
