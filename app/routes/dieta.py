"""Route for dieta"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dieta import Dieta
from app.schemas.dieta import DietaCreateSchema, DietaUpdateSchema, DietaSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/dieta", tags=["Dieta"])


@router.post("/")
async def create_dieta(dieta: DietaCreateSchema,
                       db: Session = Depends(get_db)):
    """Cria uma dieta."""
    service = BaseService(db, Dieta)
    if service.create(dieta):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{dieta_id}")
def get_dieta(dieta_id: int, db: Session = Depends(get_db)):
    """Retorna uma dieta com base no seu ID."""
    service = BaseService(db, Dieta)
    if response := service.get_by_id(dieta_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_dietas(db: Session = Depends(get_db)):
    """Retorna todos os dietas."""
    service = BaseService(db, Dieta)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{dieta_id}")
async def update_dieta(dieta_id: int, dieta: DietaUpdateSchema,
                       db: Session = Depends(get_db)):
    """Atualiza uma dieta."""
    service = BaseService(db, Dieta)
    if service.update(dieta_id, dieta):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{dieta_id}")
async def delete_dieta(dieta_id: int, db: Session = Depends(get_db)):
    """Deleta uma dieta."""
    service = BaseService(db, Dieta)
    if service.delete(dieta_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
