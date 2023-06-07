"""Routes for usuario"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.usuario import UsuarioCreateSchema, UsuarioDeleteSchema, \
    UsuarioSchema, UsuarioUpdateSchema
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuario", tags=["Usuario"])


@router.post("/", response_model=UsuarioSchema)
async def create_usuario(usuario: UsuarioCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um usuario."""
    usuario_service = UsuarioService(db)
    return usuario_service.create_usuario(usuario)


@router.get("/{usuario_id}", response_model=UsuarioSchema)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Retorna um usuario com base no seu ID."""
    usuario_service = UsuarioService(db)
    return usuario_service.get_usuario(usuario_id)


@router.get("/")
async def get_all_usuarios(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    usuario_service = UsuarioService(db)
    return usuario_service.get_all_usuarios()


@router.patch("/usuario/{usuario_id}")
async def update_usuario(usuario_id: int, usuario: UsuarioUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um usuario."""
    usuario_service = UsuarioService(db)
    return usuario_service.update_usuario(usuario_id, usuario)


@router.delete("/usuario/{usuario_id}")
async def delete_usuario(usuario: UsuarioDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um usuario."""
    usuario_service = UsuarioService(db)
    usuario_service.delete_usuario(usuario)
    return {"message": "Usuario deleted"}
