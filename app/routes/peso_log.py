"""Routes for peso_log"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.peso_log import PesoLogCreateSchema, PesoLogDeleteSchema, \
    PesoLogSchema, PesoLogUpdateSchema
from app.services.peso_log_service import PesoLogService

router = APIRouter(prefix="/peso_log", tags=["PesoLog"])


@router.post("/", response_model=PesoLogSchema)
async def create_peso_log(peso_log: PesoLogCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um peso_log."""
    peso_log_service = PesoLogService(db)
    return peso_log_service.create_peso_log(peso_log)


@router.get("/{peso_log_id}", response_model=PesoLogSchema)
def get_peso_log(peso_log_id: int, db: Session = Depends(get_db)):
    """Retorna um peso_log com base no seu ID."""
    peso_log_service = PesoLogService(db)
    return peso_log_service.get_peso_log(peso_log_id)


@router.get("/")
async def get_all_peso_logs(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    peso_log_service = PesoLogService(db)
    return peso_log_service.get_all_peso_logs()


@router.patch("/peso_log/{peso_log_id}")
async def update_peso_log(peso_log_id: int, peso_log: PesoLogUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um peso_log."""
    peso_log_service = PesoLogService(db)
    return peso_log_service.update_peso_log(peso_log_id, peso_log)


@router.delete("/peso_log/{peso_log_id}")
async def delete_peso_log(peso_log: PesoLogDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um peso_log."""
    peso_log_service = PesoLogService(db)
    peso_log_service.delete_peso_log(peso_log)
    return {"message": "PesoLog deleted"}
