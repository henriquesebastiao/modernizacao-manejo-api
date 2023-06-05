from sqlalchemy.orm import Session

from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate


def create(cargo: CargoCreate, db: Session):
    cargo_db = Cargo(cargo.parse_obj())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    return db.query(Cargo).all()


def get_byid(cargo_id: int, db: Session):
    return db.query(Cargo).filter(Cargo.id == cargo_id).first()


def update(cargo_id: int, animal: CargoCreate, db: Session):
    animal_db = db.query(Cargo).filter(Cargo.id == cargo_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(cargo_id: int, db: Session):
    animal_db = db.query(Cargo).filter(Cargo.id == cargo_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

