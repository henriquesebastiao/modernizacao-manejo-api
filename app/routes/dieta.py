"""Route for dieta"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dieta import Dieta
from app.schemas.dieta import DietaCreateSchema, DietaSchema, DietaUpdateSchema
from app.controllers.base_controller import Basecontrollers

router = APIRouter(prefix="/dieta", tags=["Dieta"])


@router.post("/", status_code=201)
async def create_dieta(dieta: DietaCreateSchema,
                       db: Session = Depends(get_db)):
    """Cria uma dieta."""
    controller = Basecontrollers(db, Dieta)
    if controller.create(dieta):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{dieta_id}", response_model=DietaSchema)
def get_dieta(dieta_id: int, db: Session = Depends(get_db)):
    """Retorna uma dieta com base no seu ID."""
    controller = Basecontrollers(db, Dieta)
    if response := controller.get_by_id(dieta_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[DietaSchema])
async def get_all_dietas(db: Session = Depends(get_db)):
    """Retorna todos os dietas."""
    controller = Basecontrollers(db, Dieta)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{dieta_id}")
async def update_dieta(dieta_id: int, dieta: DietaUpdateSchema,
                       db: Session = Depends(get_db)):
    """Atualiza uma dieta."""
    controller = Basecontrollers(db, Dieta)
    if controller.update(dieta_id, dieta):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{dieta_id}")
async def delete_dieta(dieta_id: int, db: Session = Depends(get_db)):
    """Deleta uma dieta."""
    controller = Basecontrollers(db, Dieta)
    if controller.delete(dieta_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
