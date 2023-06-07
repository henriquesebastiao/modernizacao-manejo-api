"""Rotas para o CRUD de Peso Log."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.peso_log import PesoLogCreate

router = APIRouter()


@router.post("/pesagem/")
async def create_pesagem(pesagem: PesoLogCreate, db: Session = Depends(get_db)):
    """Cria uma pesagem."""
    return registrar_peso(pesagem, db)
