from database.db import session
from models.animal import Animal
from schemas.animal import AnimalCreate


def create(animal: AnimalCreate):
    animal_db = Animal(
        chip=animal.chip,
        brinco=animal.brinco,
        origem=animal.origem,
        raca=animal.raca,
        id_mae=animal.id_mae,
        id_pai=animal.id_pai,
        sexo=animal.sexo,
        data_entrada=animal.data_entrada,
        data_nascimento=animal.data_nascimento,
        peso_nascimento=animal.peso_nascimento
    )

    session.add(animal_db)
    session.commit()
    session.refresh(animal_db)
    session.close()

    return animal_db


def get_all():
    return session.query(Animal).all()


def get_byid(animal_id: int):
    return session.query(Animal).filter(Animal.id == animal_id).first()


def update(animal_id: int, animal: AnimalCreate):
    animal_db = session.query(Animal).filter(Animal.id == animal_id).first()
    animal_db.origem = animal.origem
    animal_db.id_mae = animal.id_mae
    animal_db.id_pai = animal.id_pai
    animal_db.sexo = animal.sexo
    animal_db.data_entrada = animal.data_entrada
    animal_db.peso_nascimento = animal.peso_nascimento
    session.commit()
    session.close()
    return animal_db


def delete(animal_id: int):
    animal_db = session.query(Animal).filter(Animal.id == animal_id).first()
    session.delete(animal_db)
    session.commit()
    return animal_db
