from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base import BaseControllers
from app.database import get_db
from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreateSchema, PessoaSchema, \
    PessoaUpdateSchema

router = APIRouter(prefix="/pessoa", tags=["Pessoa"])


@router.post("/", status_code=201)
async def create(pessoa: PessoaCreateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Pessoa)
    if controller.create(pessoa):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{pessoa_id}", response_model=PessoaSchema)
def get(pessoa_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Pessoa)
    if response := controller.get_by_id(pessoa_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[PessoaSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, Pessoa)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{pessoa_id}")
async def update(pessoa_id: int, pessoa: PessoaUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, Pessoa)
    if controller.update(pessoa_id, pessoa):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{pessoa_id}")
async def delete(pessoa_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, Pessoa)
    if controller.delete(pessoa_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
