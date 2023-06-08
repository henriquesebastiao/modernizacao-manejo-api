"""Routes for raca"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.raca import Raca
from app.schemas.raca import RacaCreateSchema, RacaUpdateSchema
from app.services.base_service import BaseService

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/")
async def create_raca(raca: RacaCreateSchema, db: Session = Depends(get_db)):
    """Cria um raca."""
    service = BaseService(db, Raca)
    if service.create(raca):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{raca_id}")
def get_raca(raca_id: int, db: Session = Depends(get_db)):
    """Retorna um raca com base no seu ID."""
    service = BaseService(db, Raca)
    if response := service.get_by_id(raca_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_racas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = BaseService(db, Raca)
    if response := service.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/raca/{raca_id}")
async def update_raca(raca_id: int, raca: RacaUpdateSchema,
                      db: Session = Depends(get_db)):
    """Atualiza um raca."""
    service = BaseService(db, Raca)
    if service.update(raca_id, raca):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/raca/{raca_id}")
async def delete_raca(raca_id: int, db: Session = Depends(get_db)):
    """Deleta um raca."""
    service = BaseService(db, Raca)
    if service.delete(raca_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
