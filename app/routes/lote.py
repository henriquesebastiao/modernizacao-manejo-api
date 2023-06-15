from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base import BaseControllers
from app.database import get_db
from app.models.lote import Lote
from app.schemas.lote import LoteCreateSchema, LoteSchema, LoteUpdateSchema

router = APIRouter(prefix="/lote", tags=["Lote"])


@router.post("/", status_code=201)
async def create(lote: LoteCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Lote)
    if controller.create(lote):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{lote_id}", response_model=LoteSchema)
def get(lote_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Lote)
    if response := controller.get_by_id(lote_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[LoteSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Lote)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{lote_id}")
async def update(lote_id: int, lote: LoteUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Lote)
    if controller.update(lote_id, lote):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{lote_id}")
async def delete(lote_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Lote)
    if controller.delete(lote_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
