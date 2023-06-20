from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.pessoa import PessoaRepository
from app.schemas.pessoa import PessoaCreate, PessoaSchema, PessoaUpdate

router = APIRouter(prefix="/pessoa", tags=["Pessoa"])


@router.post("/", response_model=PessoaSchema, status_code=201)
async def create(cargo: PessoaCreate, db: AsyncSession = Depends(get_session)):
    repository = PessoaRepository(db)
    return await repository.create(cargo)


@router.get("/{pessoa_id}", response_model=PessoaSchema)
async def get_by_id(pessoa_id: int, db: AsyncSession = Depends(get_session)):
    repository = PessoaRepository(db)
    return await repository.get_by_id(pessoa_id)


@router.get("/", response_model=list[PessoaSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = PessoaRepository(db)
    return await repository.get_all()


@router.patch("/{pessoa_id}")
async def update(pessoa_id: int, pessoa: PessoaUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = PessoaRepository(db)
    return await repository.update(pessoa_id, pessoa)


@router.delete("/{pessoa_id}")
async def delete(pessoa_id: int, db: AsyncSession = Depends(get_session)):
    repository = PessoaRepository(db)
    return await repository.delete(pessoa_id)
