"""CRUD para o modelo Animal."""

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.lote_log import LoteLog
from app.models.peso_log import PesoLog
from app.schemas.animal import AnimalCreate


def create(animal: AnimalCreate, db: Session):
    """Cria um animal."""
    animal_db = Animal(**animal.dict())
    PesoLog(animal=animal_db, peso=animal.peso, data=animal.data_entrada)
    LoteLog(animal=animal_db, lote_id=animal.lote_id,
            data_entrada=animal.data_entrada)
    db.add(animal_db)
    db.commit()
    return None


def get_all(db: Session):
    """Retorna todos os animais."""
    return db.query(Animal).all()


def get_by_id(animal_id: int, db: Session):
    """Retorna um animal pelo id."""
    return db.get(Animal, animal_id)


def get_by_brinco(brinco: str, db: Session):
    """Retorna um animal pelo id."""
    return db.query(Animal).filter_by(brinco=brinco).first()


def get_by_chip(chip: str, db: Session):
    """Retorna um animal pelo id."""
    return db.query(Animal).filter_by(chip=chip).first()


def update(animal_id: int, animal: AnimalCreate, db: Session):
    """Atualiza um animal."""
    animal_db = get_by_id(animal_id, db)
    animal_db(**animal.dict())
    db.commit()
    return None


def delete(animal_id: int, db: Session):
    """Deleta um animal."""
    animal_db = get_by_id(animal_id, db)
    db.delete(animal_db)
    db.commit()
    return None
