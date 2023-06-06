"""Rotas para o CRUD de Propriedade."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.propriedade import Propriedade
from app.schemas.propriedade import PropriedadeCreate

router = APIRouter()


@router.post("/propriedade")
async def create_propriedade(propriedade: PropriedadeCreate, db: Session = Depends(get_db)):
    """Cria uma propriedade."""
    propriedade_db = Propriedade(
        nome=propriedade.nome,  # Verificar se o tratamento de string é feito no front ou no back =)
        fazendeiro_id=propriedade.fazendeiro_id
    )

    db.add(propriedade_db)
    db.commit()

    return {"message": f"Propriedade {propriedade.nome} criada com sucesso!"}


@router.get("/propriedade")
async def get_all_propriedade(db: Session = Depends(get_db)):
    """Retorna todas as propriedades."""
    return db.query(Propriedade).all()


@router.get("/propriedade/{propriedade_id}")
async def get_propriedade_by_id(propriedade_id: int, db: Session = Depends(get_db)):
    """Retorna uma propriedade pelo id."""
    return db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()


@router.put("/propriedade/{propriedade_id}")
async def update_propriedade(propriedade_id: int, propriedade: PropriedadeCreate, db: Session = Depends(get_db)):
    """Atualiza uma propriedade."""
    propriedade_db = db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()
    propriedade_db.nome = propriedade.nome
    propriedade_db.fazendeiro_id = propriedade.fazendeiro_id

    db.commit()

    return {"message": f"Propriedade {propriedade.nome} atualizada com sucesso!"}


@router.delete("/propriedade/{propriedade_id}")
async def delete_propriedade(propriedade_id: int, db: Session = Depends(get_db)):
    """Deleta uma propriedade."""
    propriedade_db = db.query(Propriedade).filter(Propriedade.id == propriedade_id).first()
    db.delete(propriedade_db)
    db.commit()

    return {"message": f"Propriedade {propriedade_db.nome} deletada com sucesso!"}
