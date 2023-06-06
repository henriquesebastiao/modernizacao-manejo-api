"""CRUD para o modelo de raça."""

from sqlalchemy.orm import Session

from app.models.raca import Raca
from app.schemas.raca import RacaCreate


def create(raca: RacaCreate, db: Session):
    """Cria uma raça."""
    raca_db = Raca(**raca.dict())
    db.add(raca_db)
    db.commit()
    return None


def get_all(db: Session):
    """Retorna todas as raças."""
    return db.query(Raca).all()


def get_by_id(raca_id: int, db: Session):
    """Retorna uma raça pelo id."""
    return db.get(Raca, raca_id)


def delete(raca_id: int, db: Session):
    """Deleta uma raça."""
    raca_db = get_by_id(raca_id, db)
    db.delete(raca_db)
    db.commit()
    return None
