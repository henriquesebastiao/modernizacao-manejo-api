from fastapi import APIRouter, Depends

from app.schemas.lote import LoteCreate, LoteSchema, LoteUpdate
from app.services.lote import LoteService

router = APIRouter(prefix="/lote", tags=["Lote"])


@router.post("/", response_model=LoteSchema, status_code=201)
async def create(lote: LoteCreate, service=Depends(LoteService)):
    return service.create(lote)


@router.get("/{lote_id}", response_model=LoteSchema)
def get_by_id(lote_id: int, service=Depends(LoteService)):
    return service.get_by_id(lote_id)


@router.get("/", response_model=list[LoteSchema])
async def get_all(service=Depends(LoteService)):
    return service.get_all()


@router.patch("/{lote_id}")
async def update(lote_id: int, lote: LoteUpdate,
                 service=Depends(LoteService)):
    return service.update(lote_id, lote)


@router.delete("/{lote_id}")
async def delete(lote_id: int, service=Depends(LoteService)) -> dict:
    return service.delete(lote_id)
