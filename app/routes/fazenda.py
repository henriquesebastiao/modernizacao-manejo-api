"""Routes for fazenda"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.fazenda import Fazenda
from app.schemas.fazenda import FazendaCreateSchema, FazendaSchema, \
    FazendaUpdateSchema
from app.controllers.base_controller import BaseControllers

router = APIRouter(prefix="/fazenda", tags=["Fazenda"])


@router.post("/", status_code=201)
async def create_fazenda(fazenda: FazendaCreateSchema,
                         db: Session = Depends(get_db)):
    """Cria um fazenda."""
    controller = BaseControllers(db, Fazenda)
    if controller.create(fazenda):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{fazenda_id}", response_model=FazendaSchema)
def get_fazenda(fazenda_id: int, db: Session = Depends(get_db)):
    """Retorna um fazenda com base no seu ID."""
    controller = BaseControllers(db, Fazenda)
    if response := controller.get_by_id(fazenda_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[FazendaSchema])
async def get_all_fazendas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    controller = BaseControllers(db, Fazenda)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/fazenda/{fazenda_id}")
async def update_fazenda(fazenda_id: int, fazenda: FazendaUpdateSchema,
                         db: Session = Depends(get_db)):
    """Atualiza um fazenda."""
    controller = BaseControllers(db, Fazenda)
    if controller.update(fazenda_id, fazenda):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/fazenda/{fazenda_id}")
async def delete_fazenda(fazenda_id: int, db: Session = Depends(get_db)):
    """Deleta um fazenda."""
    controller = BaseControllers(db, Fazenda)
    if controller.delete(fazenda_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
