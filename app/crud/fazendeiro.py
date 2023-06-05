from sqlalchemy.orm import Session

from app.models.fazendeiro import Fazendeiro
from app.schemas.fazendeiro import FazendeiroCreate


def create(cargo: FazendeiroCreate, db: Session):
    cargo_db = Fazendeiro(cargo.parse_obj())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    return db.query(Fazendeiro).all()


def get_byid(fazendeiro_id: int, db: Session):
    return db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()


def update(fazendeiro_id: int, animal: FazendeiroCreate, db: Session):
    animal_db = db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(fazendeiro_id: int, db: Session):
    animal_db = db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

