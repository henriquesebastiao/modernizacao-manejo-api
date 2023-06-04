from fastapi import APIRouter

from database.db import session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate

router = APIRouter()


@router.post("/usuario")
async def create_usuario(usuario: UsuarioCreate):
    usuario_db = Usuario(
        email=usuario.email,
        password=usuario.password,
        pessoa_id=usuario.pessoa_id
    )

    session.add(usuario_db)
    session.commit()

    return {"message": f"Usuario {usuario.email} criado com sucesso!"}


@router.delete("/usuario/{id}")
async def delete_usuario(id: int):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    session.delete(usuario_db)
    session.commit()
    return {"message": f"Usuario {usuario_db.email} deletado com sucesso!"}
