"""Routes for pessoa"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreateSchema, PessoaUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/pessoa", tags=["Pessoa"])


@router.post("/")
async def create_pessoa(pessoa: PessoaCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um pessoa."""
    service = BaseService(db, Pessoa)
    if service.create(pessoa):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{pessoa_id}")
def get_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    """Retorna um pessoa com base no seu ID."""
    service = BaseService(db, Pessoa)
    if response := service.get_by_id(pessoa_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_pessoas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, Pessoa)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/pessoa/{pessoa_id}")
async def update_pessoa(pessoa_id: int, pessoa: PessoaUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um pessoa."""
    service = BaseService(db, Pessoa)
    if service.update(pessoa_id, pessoa):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/pessoa/{pessoa_id}")
async def delete_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    """Deleta um pessoa."""
    service = BaseService(db, Pessoa)
    if service.delete(pessoa_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
