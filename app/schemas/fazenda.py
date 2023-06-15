from pydantic import BaseModel


class FazendaSchemaBase(BaseModel):
    fazendeiro_id: int
    nome: str


class FazendaCreate(FazendaSchemaBase):
    ...


class FazendaUpdate(FazendaSchemaBase):
    ...


class FazendaDelete(FazendaSchemaBase):
    ...


class FazendaSchema(FazendaSchemaBase):
    id: int
