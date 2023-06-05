from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate


def create(cargo: UsuarioCreate, db: Session):
    cargo_db = Usuario(cargo.parse_obj())
    db.add(cargo_db)
    db.commit()
    return cargo_db


def get_all(db: Session):
    return db.query(Usuario).all()


def get_byid(usuario_id: int, db: Session):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def update(usuario_id: int, animal: UsuarioCreate, db: Session):
    animal_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    animal_db(animal.parse_obj())
    db.commit()
    return animal_db


def delete(usuario_id: int, db: Session):
    animal_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

