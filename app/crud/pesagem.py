"""CRUD para o modelo de pesagem."""

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.pesagem import Pesagem
from app.schemas.pesagem import PesagemCreate


def registrar_pesagem(animal_id, data, peso, db: Session):
    """Registra uma pesagem."""
    animal = db.query(Animal).get(animal_id)
    if animal:
        peso_historico = Pesagem(animal_id=animal_id, data=data, peso=peso)
        db.add(peso_historico)
        animal.peso = peso
        db.commit()
        return peso_historico
    return None
