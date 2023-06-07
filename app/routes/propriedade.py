"""Routes for propriedade"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.propriedade import PropriedadeCreateSchema, PropriedadeDeleteSchema, \
    PropriedadeSchema, PropriedadeUpdateSchema
from app.services.propriedade_service import PropriedadeService

router = APIRouter(prefix="/propriedade", tags=["Propriedade"])


@router.post("/", response_model=PropriedadeSchema)
async def create_propriedade(propriedade: PropriedadeCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um propriedade."""
    propriedade_service = PropriedadeService(db)
    return propriedade_service.create_propriedade(propriedade)


@router.get("/{propriedade_id}", response_model=PropriedadeSchema)
def get_propriedade(propriedade_id: int, db: Session = Depends(get_db)):
    """Retorna um propriedade com base no seu ID."""
    propriedade_service = PropriedadeService(db)
    return propriedade_service.get_propriedade(propriedade_id)


@router.get("/")
async def get_all_propriedades(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    propriedade_service = PropriedadeService(db)
    return propriedade_service.get_all_propriedades()


@router.patch("/propriedade/{propriedade_id}")
async def update_propriedade(propriedade_id: int, propriedade: PropriedadeUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um propriedade."""
    propriedade_service = PropriedadeService(db)
    return propriedade_service.update_propriedade(propriedade_id, propriedade)


@router.delete("/propriedade/{propriedade_id}")
async def delete_propriedade(propriedade: PropriedadeDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um propriedade."""
    propriedade_service = PropriedadeService(db)
    propriedade_service.delete_propriedade(propriedade)
    return {"message": "Propriedade deleted"}
