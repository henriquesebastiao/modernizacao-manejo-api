"""Rotas para o CRUD de pesagem."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.pesagem import registrar_pesagem
from app.database import get_db
from app.schemas.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/")
async def create_pesagem(pesagem: PesagemCreate, db: Session = Depends(get_db)):
    """Cria uma pesagem."""
    return registrar_pesagem(pesagem, db)
