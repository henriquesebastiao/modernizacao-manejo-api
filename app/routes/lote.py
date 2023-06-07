"""Routes for lote"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.lote import LoteCreateSchema, LoteDeleteSchema, \
    LoteSchema, LoteUpdateSchema
from app.services.lote_service import LoteService

router = APIRouter(prefix="/lote", tags=["Lote"])


@router.post("/", response_model=LoteSchema)
async def create_lote(lote: LoteCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um lote."""
    lote_service = LoteService(db)
    return lote_service.create_lote(lote)


@router.get("/{lote_id}", response_model=LoteSchema)
def get_lote(lote_id: int, db: Session = Depends(get_db)):
    """Retorna um lote com base no seu ID."""
    lote_service = LoteService(db)
    return lote_service.get_lote(lote_id)


@router.get("/")
async def get_all_lotes(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    lote_service = LoteService(db)
    return lote_service.get_all_lotes()


@router.patch("/lote/{lote_id}")
async def update_lote(lote_id: int, lote: LoteUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um lote."""
    lote_service = LoteService(db)
    return lote_service.update_lote(lote_id, lote)


@router.delete("/lote/{lote_id}")
async def delete_lote(lote: LoteDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um lote."""
    lote_service = LoteService(db)
    lote_service.delete_lote(lote)
    return {"message": "Lote deleted"}
