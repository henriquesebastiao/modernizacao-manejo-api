"""CRUD para o modelo de pesagem."""

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.pesagem import Pesagem
from app.schemas.pesagem import PesagemCreate


def registrar_pesagem(pesagem: PesagemCreate, db: Session):
    """Registra uma pesagem."""
    animal = db.query(Animal).get(pesagem.animal_id)
    pesagem_db = Pesagem(**pesagem.dict())
    db.add(pesagem_db)
    animal.peso = pesagem_db.peso
    db.commit()
    return None
