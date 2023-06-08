"""Routes for fazenda"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.fazenda import Fazenda
from app.schemas.fazenda import FazendaCreateSchema, FazendaUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/")
async def create_fazenda(fazenda: FazendaCreateSchema,
                         db: Session = Depends(get_db)):
    """Cria um fazenda."""
    service = BaseService(db, Fazenda)
    if service.create(fazenda):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{fazenda_id}")
def get_fazenda(fazenda_id: int, db: Session = Depends(get_db)):
    """Retorna um fazenda com base no seu ID."""
    service = BaseService(db, Fazenda)
    if response := service.get_by_id(fazenda_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_fazendas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, Fazenda)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/fazenda/{fazenda_id}")
async def update_fazenda(fazenda_id: int, fazenda: FazendaUpdateSchema,
                         db: Session = Depends(get_db)):
    """Atualiza um fazenda."""
    service = BaseService(db, Fazenda)
    if service.update(fazenda_id, fazenda):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/fazenda/{fazenda_id}")
async def delete_fazenda(fazenda_id: int, db: Session = Depends(get_db)):
    """Deleta um fazenda."""
    service = BaseService(db, Fazenda)
    if service.delete(fazenda_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
