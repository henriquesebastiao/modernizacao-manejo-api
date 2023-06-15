from pydantic import BaseModel


class FazendaSchemaBase(BaseModel):
    fazendeiro_id: int
    nome: str


class FazendaCreateSchema(FazendaSchemaBase):
    ...


class FazendaUpdateSchema(FazendaSchemaBase):
    ...


class FazendaDeleteSchema(FazendaSchemaBase):
    ...


class FazendaSchema(FazendaSchemaBase):
    id: int
