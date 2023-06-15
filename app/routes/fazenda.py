from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base import BaseControllers
from app.database import get_db
from app.models.fazenda import Fazenda
from app.schemas.fazenda import FazendaCreateSchema, FazendaSchema, \
    FazendaUpdateSchema

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/", status_code=201)
async def create(fazenda: FazendaCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazenda)
    if controller.create(fazenda):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{fazenda_id}", response_model=FazendaSchema)
def get(fazenda_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazenda)
    if response := controller.get_by_id(fazenda_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[FazendaSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazenda)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{fazenda_id}")
async def update(fazenda_id: int, fazenda: FazendaUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazenda)
    if controller.update(fazenda_id, fazenda):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{fazenda_id}")
async def delete(fazenda_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazenda)
    if controller.delete(fazenda_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
