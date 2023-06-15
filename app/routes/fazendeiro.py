from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.database import get_db
from app.models.fazendeiro import Fazendeiro
from app.schemas.fazendeiro import FazendeiroCreateSchema, FazendeiroSchema, \
    FazendeiroUpdateSchema

router = APIRouter(prefix="/fazendeiro", tags=["Fazendeiro"])


@router.post("/", status_code=201)
async def create(cargo: FazendeiroCreateSchema,
                 db: Session = Depends(get_db)):
    controller = FazendeiroController(db, Fazendeiro)
    if controller.create(cargo):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{cargo_id}", response_model=FazendeiroSchema)
def get(cargo_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazendeiro)
    if response := controller.get_by_id(cargo_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[FazendeiroSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazendeiro)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{cargo_id}")
async def update(cargo_id: int, cargo: FazendeiroUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazendeiro)
    if controller.update(cargo_id, cargo):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{cargo_id}")
async def delete(cargo_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Fazendeiro)
    if controller.delete(cargo_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
