from sqlalchemy.orm import Session

from app.models.fazenda import Fazenda
from app.schemas.fazenda import FazendaCreate


def create(cargo: FazendaCreate, db: Session):
    cargo_db = Fazenda(cargo.parse_obj())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    return db.query(Fazenda).all()


def get_byid(fazenda_id: int, db: Session):
    return db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()


def update(fazenda_id: int, animal: FazendaCreate, db: Session):
    animal_db = db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(fazenda_id: int, db: Session):
    animal_db = db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

