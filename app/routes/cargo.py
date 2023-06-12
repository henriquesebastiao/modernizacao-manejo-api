from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.database import get_db
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreateSchema, CargoSchema, CargoUpdateSchema

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/", status_code=201)
async def create(cargo: CargoCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Cargo)
    if controller.create(cargo):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{cargo_id}", response_model=CargoSchema)
def get(cargo_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Cargo)
    if response := controller.get_by_id(cargo_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[CargoSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Cargo)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{cargo_id}")
async def update(cargo_id: int, cargo: CargoUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Cargo)
    if controller.update(cargo_id, cargo):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{cargo_id}")
async def delete(cargo_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Cargo)
    if controller.delete(cargo_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
