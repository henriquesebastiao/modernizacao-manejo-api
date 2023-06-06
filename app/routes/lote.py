"""Rotas para o CRUD de Lote"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.lote import Lote
from app.schemas.lote import LoteCreate

router = APIRouter()


@router.post("/lote")
async def create_lote(lote: LoteCreate, db: Session = Depends(get_db)):
    """Cria um lote."""
    lote_db = Lote(**lote.dict())

    db.add(lote_db)
    db.commit()

    return {"message": f"Lote {lote_db.nome} criado com sucesso!"}
