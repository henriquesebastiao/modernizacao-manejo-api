from fastapi import APIRouter, Depends

from app.schemas.propriedade import PropriedadeCreate, PropriedadeSchema, \
    PropriedadeUpdate
from app.services.propriedade import PropriedadeService

router = APIRouter(prefix="/propriedade", tags=["Propriedade"])


@router.post("/", response_model=PropriedadeSchema, status_code=201)
async def create(cargo: PropriedadeCreate, service=Depends(PropriedadeService)):
    return service.create(cargo)


@router.get("/{propriedade_id}", response_model=PropriedadeSchema)
def get_by_id(propriedade_id: int, service=Depends(PropriedadeService)):
    return service.get_by_id(propriedade_id)


@router.get("/", response_model=list[PropriedadeSchema])
async def get_all(service=Depends(PropriedadeService)):
    return service.get_all()


@router.patch("/{propriedade_id}")
async def update(propriedade_id: int, propriedade: PropriedadeUpdate,
                 service=Depends(PropriedadeService)):
    return service.update(propriedade_id, propriedade)


@router.delete("/{propriedade_id}")
async def delete(propriedade_id: int,
                 service=Depends(PropriedadeService)) -> dict:
    return service.delete(propriedade_id)
