from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.database import get_db
from app.models.propriedade import Propriedade
from app.schemas.propriedade import PropriedadeCreateSchema, PropriedadeSchema, \
    PropriedadeUpdateSchema

router = APIRouter(prefix="/propriedade", tags=["Propriedade"])


@router.post("/", status_code=201)
async def create(propriedade: PropriedadeCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Propriedade)
    if controller.create(propriedade):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{propriedade_id}", response_model=PropriedadeSchema)
def get(propriedade_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Propriedade)
    if response := controller.get_by_id(propriedade_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[PropriedadeSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Propriedade)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{propriedade_id}")
async def update(propriedade_id: int,
                 propriedade: PropriedadeUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Propriedade)
    if controller.update(propriedade_id, propriedade):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{propriedade_id}")
async def delete(propriedade_id: int,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Propriedade)
    if controller.delete(propriedade_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
