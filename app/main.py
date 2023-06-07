"""Modulo principal da aplicação."""

from fastapi import FastAPI

from app.database import Base, engine
from app.routes import animal, cargo, fazenda, fazendeiro, lote, lote_log, \
    peso_log, propriedade, raca, usuario
from app.routes import pessoa

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Cria as tabelas do banco de dados."""
    Base.metadata.create_all(engine)


app.include_router(animal.router)
app.include_router(cargo.router)
app.include_router(fazenda.router)
app.include_router(fazendeiro.router)
app.include_router(lote.router)
app.include_router(lote_log.router)
app.include_router(peso_log.router)
app.include_router(pessoa.router)
app.include_router(usuario.router)
app.include_router(propriedade.router)
app.include_router(raca.router)
