from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.propriedade import PropriedadeRepository
from app.schemas.propriedade import PropriedadeCreate, PropriedadeSchema, \
    PropriedadeUpdate

router = APIRouter(prefix="/propriedade", tags=["Propriedade"])


@router.post("/", response_model=PropriedadeSchema, status_code=201)
async def create(cargo: PropriedadeCreate,
                 db: AsyncSession = Depends(get_session)):
    repository = PropriedadeRepository(db)
    return await repository.create(cargo)


@router.get("/{propriedade_id}", response_model=PropriedadeSchema)
async def get_by_id(propriedade_id: int, db: AsyncSession = Depends(get_session)):
    repository = PropriedadeRepository(db)
    return await repository.get_by_id(propriedade_id)


@router.get("/", response_model=list[PropriedadeSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = PropriedadeRepository(db)
    return await repository.get_all()


@router.patch("/{propriedade_id}")
async def update(propriedade_id: int, propriedade: PropriedadeUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = PropriedadeRepository(db)
    return await repository.update(propriedade_id, propriedade)


@router.delete("/{propriedade_id}")
async def delete(propriedade_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = PropriedadeRepository(db)
    return await repository.delete(propriedade_id)
