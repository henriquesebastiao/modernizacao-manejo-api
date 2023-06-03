from fastapi import FastAPI
from models.animal import Base
from serializer.animal import Animal as AnimalSerializer
from models.animal import Animal
from models.pesagem import Pesagem

from database.db import session, engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.delete("/delete")
async def delete():
    Base.metadata.drop_all(bind=engine)
    return {"message": "ok"}


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(engine)


@app.post("/animal")
async def create_animal(animal: AnimalSerializer):
    animal_db = Animal(
        origem=animal.origem,
        id_mae=animal.id_mae,
        id_pai=animal.id_pai,
        idade=animal.idade,
        sexo=animal.sexo,
        data_entrada=animal.data_entrada,
        peso_nascimento=animal.peso_nascimento
    )
    session.add(animal_db)
    session.commit()

    return {"message": f"Animal {animal.origem} criado com sucesso!"}


@app.get("/animal")
async def get_animal():
    animal = session.query(Animal).all()
    return animal


@app.get("/animal/{id}")
async def get_animal_by_id(id: int):
    animal = session.query(Animal).filter(Animal.id == id).first()
    return animal


@app.patch("/animal/{id}")
async def update_animal(id: int, animal: AnimalSerializer):
    animal_db = session.query(Animal).filter(Animal.id == id).first()
    animal_db.origem = animal.origem
    animal_db.id_mae = animal.id_mae
    animal_db.id_pai = animal.id_pai
    animal_db.idade = animal.idade
    animal_db.sexo = animal.sexo
    animal_db.data_entrada = animal.data_entrada
    animal_db.peso_nascimento = animal.peso_nascimento
    session.commit()
    return {"message": f"Animal {animal.origem} atualizado com sucesso!"}


@app.delete("/animal/{id}")
async def delete_animal(id: int):
    animal_db = session.query(Animal).filter(Animal.id == id).first()
    session.delete(animal_db)
    session.commit()
    return {"message": f"Animal {animal_db.origem} deletado com sucesso!"}

