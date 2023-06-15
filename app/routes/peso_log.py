from fastapi import APIRouter, Depends

from app.schemas.peso_log import PesoLogCreate, PesoLogSchema, PesoLogUpdate
from app.services.peso_log import PesoLogService

router = APIRouter(prefix="/peso_log", tags=["PesoLog"])


@router.post("/", response_model=PesoLogSchema, status_code=201)
async def create(cargo: PesoLogCreate, service=Depends(PesoLogService)):
    return service.create(cargo)


@router.get("/{peso_log_id}", response_model=PesoLogSchema)
def get_by_id(peso_log_id: int, service=Depends(PesoLogService)):
    return service.get_by_id(peso_log_id)


@router.get("/", response_model=list[PesoLogSchema])
async def get_all(service=Depends(PesoLogService)):
    return service.get_all()


@router.patch("/{peso_log_id}")
async def update(peso_log_id: int, peso_log: PesoLogUpdate,
                 service=Depends(PesoLogService)):
    return service.update(peso_log_id, peso_log)


@router.delete("/{peso_log_id}")
async def delete(peso_log_id: int, service=Depends(PesoLogService)) -> dict:
    return service.delete(peso_log_id)
