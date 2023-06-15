from fastapi import APIRouter, Depends

from app.schemas.dieta import DietaCreate, DietaSchema, DietaUpdate
from app.services.dieta import DietaService

router = APIRouter(prefix="/dieta", tags=["Dieta"])


@router.post("/", response_model=DietaSchema, status_code=201)
async def create(cargo: DietaCreate, service=Depends(DietaService)):
    return service.create(cargo)


@router.get("/{dieta_id}", response_model=DietaSchema)
def get_by_id(dieta_id: int, service=Depends(DietaService)):
    return service.get_by_id(dieta_id)


@router.get("/", response_model=list[DietaSchema])
async def get_all(service=Depends(DietaService)):
    return service.get_all()


@router.patch("/{dieta_id}")
async def update(dieta_id: int, dieta: DietaUpdate,
                 service=Depends(DietaService)):
    return service.update(dieta_id, dieta)


@router.delete("/{dieta_id}")
async def delete(dieta_id: int, service=Depends(DietaService)) -> dict:
    return service.delete(dieta_id)
