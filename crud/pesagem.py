from sqlalchemy import event
from sqlalchemy.orm import Session
from models.pesagem import Pesagem
from schemas.pesagem import PesagemCreate


def create(animal_id: int, pesagem: PesagemCreate, db: Session):
    peso_db = Pesagem(
        peso=pesagem.peso,
        data=pesagem.data,
        id_animal=animal_id
    )

    db.add(peso_db)
    db.commit()
    db.refresh(peso_db)

    return peso_db


def get_byid(pesagem_id: int, db: Session):
    return db.query(Pesagem).filter(Pesagem.id == pesagem_id).first()
