from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate

router = APIRouter()


@router.post("/usuario")
async def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = Usuario(
        email=usuario.email,
        password=usuario.password,
        pessoa_id=usuario.pessoa_id
    )

    db.add(usuario_db)
    db.commit()

    return {"message": f"Usuario {usuario.email} criado com sucesso!"}


@router.delete("/usuario/{id}")
async def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id == id).first()
    db.delete(usuario_db)
    db.commit()
    return {"message": f"Usuario {usuario_db.email} deletado com sucesso!"}
