"""Rotas para o CRUD de fazendeiro"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import fazendeiro
from app.database import get_db
from app.schemas.fazendeiro import FazendeiroCreate

router = APIRouter()


@router.post("/fazendeiro")
async def create_pesagem(item: FazendeiroCreate,
                         db: Session = Depends(get_db)):
    """Cria um fazendeiro."""
    return fazendeiro.create(item, db)
