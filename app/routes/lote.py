"""Routes for lote"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.lote import Lote
from app.schemas.lote import LoteCreateSchema, LoteSchema, LoteUpdateSchema
from app.controllers.base_controller import BaseService

router = APIRouter(prefix="/lote", tags=["Lote"])


@router.post("/", status_code=201)
async def create_lote(lote: LoteCreateSchema,
                      db: Session = Depends(get_db)):
    """Cria um lote."""
    service = BaseService(db, Lote)
    if service.create(lote):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{lote_id}", response_model=LoteSchema)
def get_lote(lote_id: int, db: Session = Depends(get_db)):
    """Retorna um lote com base no seu ID."""
    service = BaseService(db, Lote)
    if response := service.get_by_id(lote_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[LoteSchema])
async def get_all_lotes(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, Lote)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/lote/{lote_id}")
async def update_lote(lote_id: int, lote: LoteUpdateSchema,
                      db: Session = Depends(get_db)):
    """Atualiza um lote."""
    service = BaseService(db, Lote)
    if service.update(lote_id, lote):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/lote/{lote_id}")
async def delete_lote(lote_id: int, db: Session = Depends(get_db)):
    """Deleta um lote."""
    service = BaseService(db, Lote)
    if service.delete(lote_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
