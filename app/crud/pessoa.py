from sqlalchemy.orm import Session

from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreate


def create(cargo: PessoaCreate, db: Session):
    cargo_db = Pessoa(cargo.parse_obj())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    return db.query(Pessoa).all()


def get_byid(pessoa_id: int, db: Session):
    return db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()


def update(pessoa_id: int, animal: PessoaCreate, db: Session):
    animal_db = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(pessoa_id: int, db: Session):
    animal_db = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

