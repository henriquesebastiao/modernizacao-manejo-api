from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base import BaseControllers
from app.database import get_db
from app.models.raca import Raca
from app.schemas.raca import RacaCreateSchema, RacaSchema, RacaUpdateSchema

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/", status_code=201)
async def create(raca: RacaCreateSchema, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Raca)
    if controller.create(raca):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{raca_id}", response_model=RacaSchema)
def get(raca_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Raca)
    if response := controller.get_by_id(raca_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[RacaSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Raca)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{raca_id}")
async def update(raca_id: int, raca: RacaUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Raca)
    if controller.update(raca_id, raca):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{raca_id}")
async def delete(raca_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Raca)
    if controller.delete(raca_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
