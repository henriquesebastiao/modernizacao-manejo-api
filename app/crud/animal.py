"""CRUD para o modelo Animal."""

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.pesagem import Pesagem
from app.schemas.animal import AnimalCreate


def create(animal: AnimalCreate, db: Session):
    """Cria um animal."""
    animal_db = Animal(chip=animal.chip, brinco=animal.brinco,
                       origem=animal.origem, raca=animal.raca,
                       data_entrada=animal.data_entrada,
                       data_nascimento=animal.data_nascimento,
                       peso=animal.peso, sexo=animal.sexo)

    Pesagem(animal=animal_db, peso=animal.peso, data=animal.data_entrada)
    db.add(animal_db)
    db.commit()

    return animal_db


def get_all(db: Session):
    """Retorna todos os animais."""
    return db.query(Animal).all()


def get_byid(animal_id: int, db: Session):
    """Retorna um animal pelo id."""
    return db.query(Animal).filter(Animal.id == animal_id).first()


def update(animal_id: int, animal: AnimalCreate, db: Session):
    """Atualiza um animal."""
    animal_db = db.query(Animal).filter(Animal.id == animal_id).first()
    animal_db(**animal.dict())
    db.commit()
    return animal_db


def delete(animal_id: int, db: Session):
    """Deleta um animal."""
    animal_db = db.query(Animal).filter(Animal.id == animal_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db
