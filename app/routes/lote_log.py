"""Routes for lote_log"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.lote_log import LoteLogCreateSchema, LoteLogDeleteSchema, \
    LoteLogSchema, LoteLogUpdateSchema
from app.services.lote_log_service import LoteLogService

router = APIRouter(prefix="/lote_log", tags=["LoteLog"])


@router.post("/", response_model=LoteLogSchema)
async def create_lote_log(lote_log: LoteLogCreateSchema,
                          db: Session = Depends(get_db)):
    """Cria um lote_log."""
    lote_log_service = LoteLogService(db)
    return lote_log_service.create_lote_log(lote_log)


@router.get("/{lote_log_id}", response_model=LoteLogSchema)
def get_lote_log(lote_log_id: int, db: Session = Depends(get_db)):
    """Retorna um lote_log com base no seu ID."""
    lote_log_service = LoteLogService(db)
    return lote_log_service.get_lote_log(lote_log_id)


@router.get("/")
async def get_all_lote_logs(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    lote_log_service = LoteLogService(db)
    return lote_log_service.get_all_lote_logs()


@router.patch("/lote_log/{lote_log_id}")
async def update_lote_log(lote_log_id: int, lote_log: LoteLogUpdateSchema,
                          db: Session = Depends(get_db)):
    """Atualiza um lote_log."""
    lote_log_service = LoteLogService(db)
    return lote_log_service.update_lote_log(lote_log_id, lote_log)


@router.delete("/lote_log/{lote_log_id}")
async def delete_lote_log(lote_log: LoteLogDeleteSchema,
                          db: Session = Depends(get_db)):
    """Deleta um lote_log."""
    lote_log_service = LoteLogService(db)
    lote_log_service.delete_lote_log(lote_log)
    return {"message": "LoteLog deleted"}
