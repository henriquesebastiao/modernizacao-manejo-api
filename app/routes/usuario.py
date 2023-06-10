"""Routes for usuario"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreateSchema, UsuarioSchema, \
    UsuarioUpdateSchema
from app.controllers.base_controller import Basecontrollers

router = APIRouter(prefix="/usuario", tags=["Usuário"])


@router.post("/", status_code=201)
async def create_usuario(usuario: UsuarioCreateSchema,
                         db: Session = Depends(get_db)):
    """Cria um usuário."""
    controller = Basecontrollers(db, Usuario)
    if controller.create(usuario):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{usuario_id}", response_model=UsuarioSchema)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Retorna um usuário com base no seu ID."""
    controller = Basecontrollers(db, Usuario)
    if response := controller.get_by_id(usuario_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/", response_model=list[UsuarioSchema])
async def get_all_usuarios(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    controller = Basecontrollers(db, Usuario)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/usuario/{usuario_id}")
async def update_usuario(usuario_id: int, usuario: UsuarioUpdateSchema,
                         db: Session = Depends(get_db)):
    """Atualiza um usuário."""
    controller = Basecontrollers(db, Usuario)
    if controller.update(usuario_id, usuario):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/usuario/{usuario_id}")
async def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Deleta um usuário."""
    controller = Basecontrollers(db, Usuario)
    if controller.delete(usuario_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
