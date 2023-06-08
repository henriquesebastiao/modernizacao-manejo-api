"""Routes for lote_log"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.lote_log import LoteLog
from app.schemas.lote_log import LoteLogCreateSchema, LoteLogUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/lote_log", tags=["LoteLog"])


@router.post("/")
async def create_lote_log(lote_log: LoteLogCreateSchema,
                          db: Session = Depends(get_db)):
    """Cria um lote_log."""
    service = BaseService(db, LoteLog)
    if service.create(lote_log):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{lote_log_id}")
def get_lote_log(lote_log_id: int, db: Session = Depends(get_db)):
    """Retorna um lote_log com base no seu ID."""
    service = BaseService(db, LoteLog)
    if response := service.get_by_id(lote_log_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_lote_logs(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, LoteLog)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/lote_log/{lote_log_id}")
async def update_lote_log(lote_log_id: int, lote_log: LoteLogUpdateSchema,
                          db: Session = Depends(get_db)):
    """Atualiza um lote_log."""
    service = BaseService(db, LoteLog)
    if service.update(lote_log_id, lote_log):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/lote_log/{lote_log_id}")
async def delete_lote_log(lote_log_id: int, db: Session = Depends(get_db)):
    """Deleta um lote_log."""
    service = BaseService(db, LoteLog)
    if service.delete(lote_log_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
