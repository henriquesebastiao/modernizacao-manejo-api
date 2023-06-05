"""CRUD para o modelo de pesagem."""

from sqlalchemy.orm import Session

from app.models.pesagem import Pesagem
from app.schemas.pesagem import PesagemCreate


def create(animal_id: int, pesagem: PesagemCreate, db: Session):
    """Cria uma pesagem."""
    peso_db = Pesagem(**pesagem.dict(), animal_id=animal_id)

    db.add(peso_db)
    db.commit()
    db.refresh(peso_db)

    return peso_db


def get_byid(pesagem_id: int, db: Session):
    """Retorna uma pesagem pelo id."""
    return db.query(Pesagem).filter(Pesagem.id == pesagem_id).first()
