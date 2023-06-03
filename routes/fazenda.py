from fastapi import APIRouter

from database.db import session
from models.fazenda import Fazenda
from serializer.fazenda import FazendaCreate

router = APIRouter()


@router.post("/fazenda")
async def create_fazenda(fazenda: FazendaCreate):
    fazenda_db = Fazenda(
        fazendeiro_id=fazenda.fazendeiro_id,
        nome=fazenda.nome,
    )

    session.add(fazenda_db)
    session.commit()

    return {"message": f"Fazenda {fazenda.nome} criada com sucesso!"}


@router.delete("/fazenda/{id}")
async def delete_fazenda(id: int):
    fazenda_db = session.query(Fazenda).filter(Fazenda.id == id).first()
    session.delete(fazenda_db)
    session.commit()
    return {"message": f"Fazenda {fazenda_db.nome} deletada com sucesso!"}
