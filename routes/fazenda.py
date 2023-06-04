from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.fazenda import Fazenda
from schemas.fazenda import FazendaCreate

router = APIRouter()


@router.post("/fazenda")
async def create_fazenda(fazenda: FazendaCreate, db: Session = Depends(get_db)):
    fazenda_db = Fazenda(
        fazendeiro_id=fazenda.fazendeiro_id,
        nome=fazenda.nome,
    )

    db.add(fazenda_db)
    db.commit()

    return {"message": f"Fazenda {fazenda.nome} criada com sucesso!"}


@router.delete("/fazenda/{id}")
async def delete_fazenda(id: int, db: Session = Depends(get_db)):
    fazenda_db = db.query(Fazenda).filter(Fazenda.id == id).first()
    db.delete(fazenda_db)
    db.commit()
    return {"message": f"Fazenda {fazenda_db.nome} deletada com sucesso!"}
