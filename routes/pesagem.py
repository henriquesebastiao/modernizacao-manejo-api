from fastapi import APIRouter

from database.db import session
from models.animal import Animal
from schemas.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/{animal_id}")
async def create_pesagem(animal_id: int):
    animal_db = session.query(Animal).filter(Animal.id == animal_id).first()

    return {
        "message": f"Pesagem do animal {animal_db.origem} criada com sucesso! O id da pesagem é {peso_db.id}"}
