"""Routes for cargo"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreateSchema, CargoSchema, CargoUpdateSchema
from app.controllers.base_controller import BaseControllers

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/", status_code=201)
async def create_cargo(cargo: CargoCreateSchema,
                       db: Session = Depends(get_db)):
    """Cria um cargo."""
    controller = BaseControllers(db, Cargo)
    if controller.create(cargo):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{cargo_id}", response_model=CargoSchema)
def get_cargo(cargo_id: int, db: Session = Depends(get_db)):
    """Retorna um cargo com base no seu ID."""
    controller = BaseControllers(db, Cargo)
    if response := controller.get_by_id(cargo_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[CargoSchema])
async def get_all_cargos(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    controller = BaseControllers(db, Cargo)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/cargo/{cargo_id}")
async def update_cargo(cargo_id: int, cargo: CargoUpdateSchema,
                       db: Session = Depends(get_db)):
    """Atualiza um cargo."""
    controller = BaseControllers(db, Cargo)
    if controller.update(cargo_id, cargo):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/cargo/{cargo_id}")
async def delete_cargo(cargo_id: int, db: Session = Depends(get_db)):
    """Deleta um cargo."""
    controller = BaseControllers(db, Cargo)
    if controller.delete(cargo_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
