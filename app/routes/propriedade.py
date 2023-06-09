"""Routes for propriedade"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.propriedade import Propriedade
from app.schemas.propriedade import PropriedadeCreateSchema, PropriedadeSchema, \
    PropriedadeUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/propriedade", tags=["Propriedade"])


@router.post("/", status_code=201)
async def create_propriedade(propriedade: PropriedadeCreateSchema,
                             db: Session = Depends(get_db)):
    """Cria um propriedade."""
    service = BaseService(db, Propriedade)
    if service.create(propriedade):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{propriedade_id}", response_model=PropriedadeSchema)
def get_propriedade(propriedade_id: int, db: Session = Depends(get_db)):
    """Retorna um propriedade com base no seu ID."""
    service = BaseService(db, Propriedade)
    if response := service.get_by_id(propriedade_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[PropriedadeSchema])
async def get_all_propriedades(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, Propriedade)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/propriedade/{propriedade_id}")
async def update_propriedade(propriedade_id: int,
                             propriedade: PropriedadeUpdateSchema,
                             db: Session = Depends(get_db)):
    """Atualiza um propriedade."""
    service = BaseService(db, Propriedade)
    if service.update(propriedade_id, propriedade):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/propriedade/{propriedade_id}")
async def delete_propriedade(propriedade_id: int,
                             db: Session = Depends(get_db)):
    """Deleta um propriedade."""
    service = BaseService(db, Propriedade)
    if service.delete(propriedade_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
