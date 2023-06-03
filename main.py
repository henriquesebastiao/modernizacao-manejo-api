from fastapi import FastAPI

from database.db import engine
from models.animal import Base
from routes import animal, cargo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(engine)


app.include_router(animal.router, tags=["animal"])
app.include_router(cargo.router, tags=["cargo"])
