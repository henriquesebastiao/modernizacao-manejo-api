"""CRUD para o modelo Fazendeiro."""

from sqlalchemy.orm import Session

from app.models.fazendeiro import Fazendeiro
from app.schemas.fazendeiro import FazendeiroCreate


def create(fazendeiro: FazendeiroCreate, db: Session):
    """Cria um fazendeiro."""
    fazendeiro_db = Fazendeiro(**fazendeiro.dict())
    db.add(fazendeiro_db)
    db.commit()
    return fazendeiro_db


def get_all(db: Session):
    """Retorna todos os fazendeiros."""
    return db.query(Fazendeiro).all()


def get_byid(fazendeiro_id: int, db: Session):
    """Retorna um fazendeiro pelo id."""
    return db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()


def update(fazendeiro_id: int, animal: FazendeiroCreate, db: Session):
    """Atualiza um fazendeiro."""
    animal_db = db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(fazendeiro_id: int, db: Session):
    """Deleta um fazendeiro."""
    animal_db = db.query(Fazendeiro).filter(Fazendeiro.id == fazendeiro_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

