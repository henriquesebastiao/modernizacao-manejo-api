"""Modulo principal da aplicação."""

from fastapi import FastAPI

from app.database import Base, engine
from app.routes import animal, cargo, fazenda, fazendeiro, lote, peso_log, \
    usuario, propriedade, raca
from app.routes import pessoa

from app.models.raca import Raca
from app.models.fazenda import Fazenda
from app.models.fazendeiro import Fazendeiro
from app.models.cargo import Cargo
from app.models.pessoa import Pessoa
from app.models.usuario import Usuario
from app.models.propriedade import Propriedade
from app.models.lote import Lote
from app.models.animal import Animal
from app.models.peso_log import PesoLog
from app.models.lote_log import LoteLog


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Cria as tabelas do banco de dados."""
    Base.metadata.create_all(engine)


app.include_router(animal.router)
app.include_router(cargo.router, tags=["cargo"])
app.include_router(fazenda.router, tags=["fazenda"])
app.include_router(fazendeiro.router, tags=["fazendeiro"])
app.include_router(lote.router, tags=["lote"])
app.include_router(peso_log.router, tags=["pesagem"])
app.include_router(pessoa.router, tags=["pessoa"])
app.include_router(usuario.router, tags=["usuario"])
app.include_router(propriedade.router, tags=["propriedade"])
app.include_router(raca.router, tags=["racas"])
