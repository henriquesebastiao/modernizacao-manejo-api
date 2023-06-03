from fastapi import APIRouter

from database.db import session
from models.animal import Animal
from models.pesagem import Pesagem
from serializer.animal import AnimalCreate

router = APIRouter()


@router.post("/animal")
async def create_animal(animal: AnimalCreate):
    animal_db = Animal(
        origem=animal.origem,
        id_mae=animal.id_mae,
        id_pai=animal.id_pai,
        idade=animal.idade,
        sexo=animal.sexo,
        data_entrada=animal.data_entrada,
        peso_nascimento=animal.peso_nascimento
    )

    session.add(animal_db)
    session.commit()

    peso_db = Pesagem(
        animal_id=animal_db.id,
        peso=animal.peso_nascimento,
        data=animal.data_entrada
    )

    session.add(peso_db)
    session.commit()

    return {
        "message": f"Animal {animal.origem} criado com sucesso! O id do animal é {animal_db.id}"}


@router.get("/animal")
async def get_animal():
    animal = session.query(Animal).all()
    return animal


@router.get("/animal/{id}")
async def get_animal_by_id(id: int):
    animal = session.query(Animal).filter(Animal.id == id).first()
    return animal


@router.patch("/animal/{id}")
async def update_animal(id: int, animal: AnimalCreate):
    animal_db = session.query(Animal).filter(Animal.id == id).first()
    animal_db.origem = animal.origem
    animal_db.id_mae = animal.id_mae
    animal_db.id_pai = animal.id_pai
    animal_db.idade = animal.idade
    animal_db.sexo = animal.sexo
    animal_db.data_entrada = animal.data_entrada
    animal_db.peso_nascimento = animal.peso_nascimento
    session.commit()
    return {"message": f"Animal {animal.origem} atualizado com sucesso!"}


@router.delete("/animal/{id}")
async def delete_animal(id: int):
    animal_db = session.query(Animal).filter(Animal.id == id).first()
    session.delete(animal_db)
    session.commit()
    return {"message": f"Animal {animal_db.origem} deletado com sucesso!"}
