from fastapi import APIRouter, Depends

from app.schemas.pessoa import PessoaCreate, PessoaSchema, PessoaUpdate
from app.services.pessoa import PessoaService

router = APIRouter(prefix="/pessoa", tags=["Pessoa"])


@router.post("/", response_model=PessoaSchema, status_code=201)
async def create(cargo: PessoaCreate, service=Depends(PessoaService)):
    return service.create(cargo)


@router.get("/{pessoa_id}", response_model=PessoaSchema)
def get_by_id(pessoa_id: int, service=Depends(PessoaService)):
    return service.get(pessoa_id)


@router.get("/", response_model=list[PessoaSchema])
async def get_all(service=Depends(PessoaService)):
    return service.get_all()


@router.patch("/{pessoa_id}")
async def update(pessoa_id: int, pessoa: PessoaUpdate,
                 service=Depends(PessoaService)):
    return service.update(pessoa_id, pessoa)


@router.delete("/{pessoa_id}")
async def delete(pessoa_id: int, service=Depends(PessoaService)) -> dict:
    return service.delete(pessoa_id)
