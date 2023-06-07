"""Routes for pessoa"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.pessoa import PessoaCreateSchema, PessoaDeleteSchema, \
    PessoaSchema, PessoaUpdateSchema
from app.services.pessoa_service import PessoaService

router = APIRouter(prefix="/pessoa", tags=["Pessoa"])


@router.post("/", response_model=PessoaSchema)
async def create_pessoa(pessoa: PessoaCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um pessoa."""
    pessoa_service = PessoaService(db)
    return pessoa_service.create_pessoa(pessoa)


@router.get("/{pessoa_id}", response_model=PessoaSchema)
def get_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    """Retorna um pessoa com base no seu ID."""
    pessoa_service = PessoaService(db)
    return pessoa_service.get_pessoa(pessoa_id)


@router.get("/")
async def get_all_pessoas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    pessoa_service = PessoaService(db)
    return pessoa_service.get_all_pessoas()


@router.patch("/pessoa/{pessoa_id}")
async def update_pessoa(pessoa_id: int, pessoa: PessoaUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um pessoa."""
    pessoa_service = PessoaService(db)
    return pessoa_service.update_pessoa(pessoa_id, pessoa)


@router.delete("/pessoa/{pessoa_id}")
async def delete_pessoa(pessoa: PessoaDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um pessoa."""
    pessoa_service = PessoaService(db)
    pessoa_service.delete_pessoa(pessoa)
    return {"message": "Pessoa deleted"}
