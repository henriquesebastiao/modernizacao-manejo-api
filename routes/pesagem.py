from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import pesagem
from database.db import get_db
from schemas.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/{animal_id}")
async def create_pesagem(animal_id: int, item: PesagemCreate, db: Session = Depends(get_db)):
    return pesagem.create(animal_id, item, db)

