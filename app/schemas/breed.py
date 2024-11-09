from pydantic import BaseModel, ConfigDict


class BreedSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    name: str | None


class BreedCreateUpdate(BaseModel):
    name: str


class BreedList(BaseModel):
    breeds: list[BreedSchema]
