from database.db import session
from serializer.animal import AnimalCreate
from models.animal import Animal


def create_animal_crud(animal: AnimalCreate):
    animal_db = Animal(
        chip=animal.chip,
        brinco=animal.brinco,
        origem=animal.origem,
        raca=animal.raca,
        id_mae=animal.id_mae,
        id_pai=animal.id_pai,
        sexo=animal.sexo,
        data_entrada=animal.data_entrada,
        data_nascimento=animal.data_nascimento,
        peso_nascimento=animal.peso_nascimento
    )

    session.add(animal_db)
    session.commit()
    session.close()

    print("TESTE")
    print(animal_db.id)

    return animal_db
