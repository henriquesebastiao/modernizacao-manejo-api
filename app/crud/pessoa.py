"""CRUD de Pessoa."""

from sqlalchemy.orm import Session

from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreate


def create(pessoa: PessoaCreate, db: Session):
    """Cria uma pessoa."""
    pessoa_id = Pessoa(**pessoa.dict())
    db.add(pessoa_id)
    db.commit()
    return pessoa_id


def get_all(db: Session):
    """Retorna todas as pessoas."""
    return db.query(Pessoa).all()


def get_byid(pessoa_id: int, db: Session):
    """Retorna uma pessoa pelo id."""
    return db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()


def update(pessoa_id: int, pessoa: PessoaCreate, db: Session):
    """Atualiza uma pessoa."""
    animal_db = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    animal_db(**pessoa.dict())
    db.commit()
    return animal_db


def delete(pessoa_id: int, db: Session):
    """Deleta uma pessoa."""
    animal_db = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

