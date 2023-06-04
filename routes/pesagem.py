from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.animal import Animal
from schemas.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/{animal_id}")
async def create_pesagem(animal_id: int, db: Session = Depends(get_db)):
    animal_db = db.query(Animal).filter(Animal.id == animal_id).first()

    return {
        "message": f"Pesagem do animal {animal_db.origem}"}
