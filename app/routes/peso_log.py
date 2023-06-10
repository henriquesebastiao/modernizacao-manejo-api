"""Routes for peso_log"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.peso_log import PesoLog
from app.schemas.peso_log import PesoLogCreateSchema, PesoLogSchema, \
    PesoLogUpdateSchema
from app.controllers.base_controller import BaseControllers

router = APIRouter(prefix="/peso_log", tags=["PesoLog"])


@router.post("/", status_code=201)
async def create_peso_log(peso_log: PesoLogCreateSchema,
                          db: Session = Depends(get_db)):
    """Cria um peso_log."""
    controller = BaseControllers(db, PesoLog)
    if controller.create(peso_log):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{peso_log_id}", response_model=PesoLogSchema)
def get_peso_log(peso_log_id: int, db: Session = Depends(get_db)):
    """Retorna um peso_log com base no seu ID."""
    controller = BaseControllers(db, PesoLog)
    if response := controller.get_by_id(peso_log_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[PesoLogSchema])
async def get_all_peso_logs(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    controller = BaseControllers(db, PesoLog)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/peso_log/{peso_log_id}")
async def update_peso_log(peso_log_id: int, peso_log: PesoLogUpdateSchema,
                          db: Session = Depends(get_db)):
    """Atualiza um peso_log."""
    controller = BaseControllers(db, PesoLog)
    if controller.update(peso_log_id, peso_log):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/peso_log/{peso_log_id}")
async def delete_peso_log(peso_log_id: int, db: Session = Depends(get_db)):
    """Deleta um peso_log."""
    controller = BaseControllers(db, PesoLog)
    if controller.delete(peso_log_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
