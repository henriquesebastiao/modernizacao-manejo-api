"""CRUD de cargo."""

from sqlalchemy.orm import Session

from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate


def create(cargo: CargoCreate, db: Session):
    """Cria um cargo."""
    cargo_db = Cargo(**cargo.dict())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    """Retorna todos os cargos."""
    return db.query(Cargo).all()


def get_byid(cargo_id: int, db: Session):
    """Retorna um cargo pelo id."""
    return db.query(Cargo).filter(Cargo.id == cargo_id).first()


def update(cargo_id: int, cargo: CargoCreate, db: Session):
    """Atualiza um cargo."""
    animal_db = db.query(Cargo).filter(Cargo.id == cargo_id).first()
    animal_db(**cargo.dict())
    db.commit()
    return animal_db


def delete(cargo_id: int, db: Session):
    """Deleta um cargo."""
    animal_db = db.query(Cargo).filter(Cargo.id == cargo_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

