from database.db import session
from schemas.animal import Pesagem
from models.pesagem import Pesagem

peso_db = Pesagem(
    animal_id=animal_db.id,
    peso=pesagem.peso,
    data=pesagem.data
)

session.add(peso_db)
session.commit()