from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.fazendeiro import FazendeiroRepository
from app.schemas.fazendeiro import FazendeiroCreate, FazendeiroSchema, \
    FazendeiroUpdate

router = APIRouter(prefix="/fazendeiro", tags=["Fazendeiro"])


@router.post("/", response_model=FazendeiroSchema, status_code=201)
async def create(fazendeiro: FazendeiroCreate,
                 db: AsyncSession = Depends(get_session)):
    repository = FazendeiroRepository(db)
    return await repository.create(fazendeiro)


@router.get("/{fazendeiro_id}", response_model=FazendeiroSchema)
async def get_by_id(fazendeiro_id: int, db: AsyncSession = Depends(get_session)):
    repository = FazendeiroRepository(db)
    return await repository.get_by_id(fazendeiro_id)


@router.get("/", response_model=list[FazendeiroSchema])
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = FazendeiroRepository(db)
    return await repository.get_all()


@router.patch("/{fazendeiro_id}")
async def update(fazendeiro_id: int, fazendeiro: FazendeiroUpdate,
                 db: AsyncSession = Depends(get_session)):
    repository = FazendeiroRepository(db)
    return await repository.update(fazendeiro_id, fazendeiro)


@router.delete("/{fazendeiro_id}")
async def delete(fazendeiro_id: int,
                 db: AsyncSession = Depends(get_session)):
    repository = FazendeiroRepository(db)
    return await repository.delete(fazendeiro_id)
