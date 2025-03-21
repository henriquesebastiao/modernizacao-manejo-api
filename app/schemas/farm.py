from pydantic import BaseModel, ConfigDict


class FarmCreate(BaseModel):
    name: str


class FarmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    name: str | None


class FarmList(BaseModel):
    farms: list[FarmSchema]
