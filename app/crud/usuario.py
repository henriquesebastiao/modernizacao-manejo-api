"""CRUD de Usuário."""

from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate


def create(usuario: UsuarioCreate, db: Session):
    """Cria um usuário."""
    usuario_id = Usuario(**usuario.dict())
    db.add(usuario_id)
    db.commit()
    return usuario_id


def get_all(db: Session):
    """Retorna todos os usuários."""
    return db.query(Usuario).all()


def get_byid(usuario_id: int, db: Session):
    """Retorna um usuário pelo id."""
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def update(usuario_id: int, animal: UsuarioCreate, db: Session):
    """Atualiza um usuário."""
    animal_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    animal_db(**animal.dict())
    db.commit()
    return animal_db


def delete(usuario_id: int, db: Session):
    """Deleta um usuário."""
    animal_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.delete(animal_db)
    db.commit()
    return animal_db

