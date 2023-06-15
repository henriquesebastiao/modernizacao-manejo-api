from fastapi import APIRouter, Depends

from app.schemas.fazenda import FazendaCreate, FazendaSchema, FazendaUpdate
from app.services.fazenda import FazendaService

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/", response_model=FazendaSchema, status_code=201)
async def create(cargo: FazendaCreate, service=Depends(FazendaService)):
    return service.create(cargo)


@router.get("/{fazenda_id}", response_model=FazendaSchema)
def get_by_id(fazenda_id: int, service=Depends(FazendaService)):
    return service.get(fazenda_id)


@router.get("/", response_model=list[FazendaSchema])
async def get_all(service=Depends(FazendaService)):
    return service.get_all()


@router.patch("/{fazenda_id}")
async def update(fazenda_id: int, fazenda: FazendaUpdate,
                 service=Depends(FazendaService)):
    return service.update(fazenda_id, fazenda)


@router.delete("/{fazenda_id}")
async def delete(fazenda_id: int, service=Depends(FazendaService)) -> dict:
    return service.delete(fazenda_id)
