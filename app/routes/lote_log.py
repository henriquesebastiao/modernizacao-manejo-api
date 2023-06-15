from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base import BaseControllers
from app.database import get_db
from app.models.lote_log import LoteLog
from app.schemas.lote_log import LoteLogCreateSchema, LoteLogSchema, \
    LoteLogUpdateSchema

router = APIRouter(prefix="/lote_log", tags=["LoteLog"])


@router.post("/", status_code=201)
async def create(lote_log: LoteLogCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, LoteLog)
    if controller.create(lote_log):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{lote_log_id}", response_model=LoteLogSchema)
def get(lote_log_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, LoteLog)
    if response := controller.get_by_id(lote_log_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[LoteLogSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, LoteLog)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{lote_log_id}")
async def update(lote_log_id: int, lote_log: LoteLogUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, LoteLog)
    if controller.update(lote_log_id, lote_log):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{lote_log_id}")
async def delete(lote_log_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, LoteLog)
    if controller.delete(lote_log_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
