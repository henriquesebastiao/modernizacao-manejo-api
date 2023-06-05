from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate

router = APIRouter()


@router.post("/usuario")
async def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    return {"message": f"Usuario {usuario.email} criado com sucesso!"}


@router.delete("/usuario/{id}")
async def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id == id).first()
    db.delete(usuario_db)
    db.commit()
    return {"message": f"Usuario {usuario_db.email} deletado com sucesso!"}
