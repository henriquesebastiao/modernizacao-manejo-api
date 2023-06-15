from fastapi import APIRouter, Depends

from app.schemas.lote_log import LoteLogCreate, LoteLogSchema, LoteLogUpdate
from app.services.lote_log import LoteLogService

router = APIRouter(prefix="/lote_log", tags=["LoteLog"])


@router.post("/", response_model=LoteLogSchema, status_code=201)
async def create(cargo: LoteLogCreate, service=Depends(LoteLogService)):
    return service.create(cargo)


@router.get("/{lote_log_id}", response_model=LoteLogSchema)
def get_by_id(lote_log_id: int, service=Depends(LoteLogService)):
    return service.get(lote_log_id)


@router.get("/", response_model=list[LoteLogSchema])
async def get_all(service=Depends(LoteLogService)):
    return service.get_all()


@router.patch("/{lote_log_id}")
async def update(lote_log_id: int, lote_log: LoteLogUpdate,
                 service=Depends(LoteLogService)):
    return service.update(lote_log_id, lote_log)


@router.delete("/{lote_log_id}")
async def delete(lote_log_id: int, service=Depends(LoteLogService)) -> dict:
    return service.delete(lote_log_id)
