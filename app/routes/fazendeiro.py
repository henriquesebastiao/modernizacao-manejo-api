"""Routes for fazendeiro"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.fazendeiro import FazendeiroCreateSchema, FazendeiroDeleteSchema, \
    FazendeiroSchema, FazendeiroUpdateSchema
from app.services.fazendeiro_service import FazendeiroService

router = APIRouter(prefix="/fazendeiro", tags=["Fazendeiro"])


@router.post("/", response_model=FazendeiroSchema)
async def create_fazendeiro(fazendeiro: FazendeiroCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um fazendeiro."""
    fazendeiro_service = FazendeiroService(db)
    return fazendeiro_service.create_fazendeiro(fazendeiro)


@router.get("/{fazendeiro_id}", response_model=FazendeiroSchema)
def get_fazendeiro(fazendeiro_id: int, db: Session = Depends(get_db)):
    """Retorna um fazendeiro com base no seu ID."""
    fazendeiro_service = FazendeiroService(db)
    return fazendeiro_service.get_fazendeiro(fazendeiro_id)


@router.get("/")
async def get_all_fazendeiros(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    fazendeiro_service = FazendeiroService(db)
    return fazendeiro_service.get_all_fazendeiros()


@router.patch("/fazendeiro/{fazendeiro_id}")
async def update_fazendeiro(fazendeiro_id: int, fazendeiro: FazendeiroUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um fazendeiro."""
    fazendeiro_service = FazendeiroService(db)
    return fazendeiro_service.update_fazendeiro(fazendeiro_id, fazendeiro)


@router.delete("/fazendeiro/{fazendeiro_id}")
async def delete_fazendeiro(fazendeiro: FazendeiroDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um fazendeiro."""
    fazendeiro_service = FazendeiroService(db)
    fazendeiro_service.delete_fazendeiro(fazendeiro)
    return {"message": "Fazendeiro deleted"}
