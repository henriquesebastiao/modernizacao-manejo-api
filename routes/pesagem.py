from fastapi import APIRouter

from database.db import session
from models.animal import Animal
from models.pesagem import Pesagem
from serializer.animal import AnimalCreate
from serializer.pesagem import PesagemCreate

router = APIRouter()


@router.post("/pesagem/{id}")
async def create_pesagem(id: int, pesagem: PesagemCreate):
    animal_db = session.query(Animal).filter(Animal.id == id).first()

    peso_db = Pesagem(
        animal_id=animal_db.id,
        peso=pesagem.peso,
        data=pesagem.data
    )

    session.add(peso_db)
    session.commit()

    return {
        "message": f"Pesagem do animal {animal_db.origem} criada com sucesso! O id da pesagem é {peso_db.id}"}
