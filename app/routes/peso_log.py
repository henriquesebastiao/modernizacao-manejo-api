"""Routes for peso_log"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.peso_log import PesoLog
from app.schemas.peso_log import PesoLogCreateSchema, PesoLogUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/peso_log", tags=["PesoLog"])


@router.post("/")
async def create_peso_log(peso_log: PesoLogCreateSchema,
                          db: Session = Depends(get_db)):
    """Cria um peso_log."""
    service = BaseService(db, PesoLog)
    if service.create(peso_log):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{peso_log_id}")
def get_peso_log(peso_log_id: int, db: Session = Depends(get_db)):
    """Retorna um peso_log com base no seu ID."""
    service = BaseService(db, PesoLog)
    if response := service.get_by_id(peso_log_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_peso_logs(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, PesoLog)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/peso_log/{peso_log_id}")
async def update_peso_log(peso_log_id: int, peso_log: PesoLogUpdateSchema,
                          db: Session = Depends(get_db)):
    """Atualiza um peso_log."""
    service = BaseService(db, PesoLog)
    if service.update(peso_log_id, peso_log):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/peso_log/{peso_log_id}")
async def delete_peso_log(peso_log_id: int, db: Session = Depends(get_db)):
    """Deleta um peso_log."""
    service = BaseService(db, PesoLog)
    if service.delete(peso_log_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
