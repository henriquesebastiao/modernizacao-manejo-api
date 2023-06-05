"""Rotas para o CRUD de pesagem."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import pesagem
from app.database import get_db
from app.schemas.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/{animal_id}")
async def create_pesagem(animal_id: int, item: PesagemCreate,
                         db: Session = Depends(get_db)):
    """Cria uma pesagem."""
    return pesagem.create(animal_id, item, db)
