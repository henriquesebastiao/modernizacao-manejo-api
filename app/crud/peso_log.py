"""CRUD para o modelo de pesagem."""

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.peso_log import PesoLog
from app.schemas.peso_log import PesoLogCreate


def registrar_peso(pesagem: PesoLogCreate, db: Session):
    """Registra uma pesagem."""
    animal = db.query(Animal).get(pesagem.animal_id)
    pesagem_db = PesoLog(**pesagem.dict())
    db.add(pesagem_db)
    animal.peso = pesagem_db.peso
    db.commit()
    return None
