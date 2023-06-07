"""Routes for fazenda"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.fazenda import FazendaCreateSchema, FazendaDeleteSchema, \
    FazendaSchema, FazendaUpdateSchema
from app.services.fazenda_service import FazendaService

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/", response_model=FazendaSchema)
async def create_fazenda(fazenda: FazendaCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um fazenda."""
    fazenda_service = FazendaService(db)
    return fazenda_service.create_fazenda(fazenda)


@router.get("/{fazenda_id}", response_model=FazendaSchema)
def get_fazenda(fazenda_id: int, db: Session = Depends(get_db)):
    """Retorna um fazenda com base no seu ID."""
    fazenda_service = FazendaService(db)
    return fazenda_service.get_fazenda(fazenda_id)


@router.get("/")
async def get_all_fazendas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    fazenda_service = FazendaService(db)
    return fazenda_service.get_all_fazendas()


@router.patch("/fazenda/{fazenda_id}")
async def update_fazenda(fazenda_id: int, fazenda: FazendaUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um fazenda."""
    fazenda_service = FazendaService(db)
    return fazenda_service.update_fazenda(fazenda_id, fazenda)


@router.delete("/fazenda/{fazenda_id}")
async def delete_fazenda(fazenda: FazendaDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um fazenda."""
    fazenda_service = FazendaService(db)
    fazenda_service.delete_fazenda(fazenda)
    return {"message": "Fazenda deleted"}
