"""CRUD para a tabela fazenda."""

from sqlalchemy.orm import Session

from app.models.fazenda import Fazenda
from app.schemas.fazenda import FazendaCreate


def create(fazenda: FazendaCreate, db: Session):
    """Cria uma fazenda."""
    fazenda_db = Fazenda(**fazenda.dict())
    db.add(fazenda_db)
    db.commit()
    return fazenda_db


def get_all(db: Session):
    """Retorna todas as fazendas."""
    return db.query(Fazenda).all()


def get_byid(fazenda_id: int, db: Session):
    """Retorna uma fazenda pelo id."""
    return db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()


def update(fazenda_id: int, animal: FazendaCreate, db: Session):
    """Atualiza uma fazenda."""
    animal_db = db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(fazenda_id: int, db: Session):
    """Deleta uma fazenda."""
    animal_db = db.query(Fazenda).filter(Fazenda.id == fazenda_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

