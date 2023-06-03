from pydantic import BaseModel


class FazendaPessoa(BaseModel):
    id: int
    fazenda_id: int
    pessoa_id: int
