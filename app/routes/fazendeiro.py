from fastapi import APIRouter, Depends

from app.schemas.fazendeiro import FazendeiroCreate, FazendeiroSchema, \
    FazendeiroUpdate
from app.services.fazendeiro import FazendeiroService

router = APIRouter(prefix="/fazendeiro", tags=["Fazendeiro"])


@router.post("/", response_model=FazendeiroSchema, status_code=201)
async def create(cargo: FazendeiroCreate, service=Depends(FazendeiroService)):
    return service.create(cargo)


@router.get("/{fazendeiro_id}", response_model=FazendeiroSchema)
def get_by_id(fazendeiro_id: int, service=Depends(FazendeiroService)):
    return service.get(fazendeiro_id)


@router.get("/", response_model=list[FazendeiroSchema])
async def get_all(service=Depends(FazendeiroService)):
    return service.get_all()


@router.patch("/{fazendeiro_id}")
async def update(fazendeiro_id: int, fazendeiro: FazendeiroUpdate,
                 service=Depends(FazendeiroService)):
    return service.update(fazendeiro_id, fazendeiro)


@router.delete("/{fazendeiro_id}")
async def delete(fazendeiro_id: int,
                 service=Depends(FazendeiroService)) -> dict:
    return service.delete(fazendeiro_id)
