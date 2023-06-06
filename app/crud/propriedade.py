"""CRUD de Propriedade."""

from sqlalchemy.orm import Session

from app.models.propriedade import Propriedade
from app.schemas.propriedade import PropriedadeCreate


def create(propriedade: PropriedadeCreate, db: Session):
    """Cria uma propriedade."""
    propriedade_id = Propriedade(**propriedade.dict())
    db.add(propriedade_id)
    db.commit()
    return propriedade_id


def get_all(db: Session):
    """Retorna todas as propriedades."""
    return db.query(Propriedade).all()


def get_byid(propriedade_id: int, db: Session):
    """Retorna uma propriedade pelo id."""
    return db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()


def update(propriedade_id: int, propriedade: PropriedadeCreate, db: Session):
    """Atualiza uma propriedade."""
    propriedade_db = db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()
    propriedade_db(**propriedade.dict())
    db.commit()
    return propriedade_db


def delete(propriedade_id: int, db: Session):
    """Deleta uma propriedade."""
    propriedade_db = db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()
    db.delete(propriedade_db)
    db.commit()
    return propriedade_db