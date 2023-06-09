"""Modulo principal da aplicação."""

from fastapi import FastAPI

from app.routes import animal, cargo, fazenda, fazendeiro, lote, lote_log, \
    peso_log, propriedade, raca, usuario, dieta
from app.routes import pessoa

app = FastAPI()

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
app.include_router(dieta.router)
