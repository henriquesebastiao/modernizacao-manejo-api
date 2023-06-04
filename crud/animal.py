from sqlalchemy.orm import Session
from models.animal import Animal
from schemas.animal import AnimalCreate


def create(animal: AnimalCreate, db: Session):
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

    db.add(animal_db)
    db.commit()
    db.refresh(animal_db)

    return animal_db


def get_all(db: Session):
    return db.query(Animal).all()


def get_byid(animal_id: int, db: Session):
    return db.query(Animal).filter(Animal.id == animal_id).first()


def update(animal_id: int, animal: AnimalCreate, db: Session):
    animal_db = db.query(Animal).filter(Animal.id == animal_id).first()
    animal_db.origem = animal.origem
    animal_db.id_mae = animal.id_mae
    animal_db.id_pai = animal.id_pai
    animal_db.sexo = animal.sexo
    animal_db.data_entrada = animal.data_entrada
    animal_db.peso_nascimento = animal.peso_nascimento
    db.commit()
    return animal_db


def delete(animal_id: int, db: Session):
    animal_db = db.query(Animal).filter(Animal.id == animal_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db
