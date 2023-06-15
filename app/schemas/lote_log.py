from datetime import date

from pydantic import BaseModel


class LoteLogBase(BaseModel):
    lote_id: int | None
    data_entrada: date | None
    data_saida: date | None


class LoteLogCreate(LoteLogBase):
    ...


class LoteLogUpdate(LoteLogBase):
    ...


class LoteLogDelete(LoteLogBase):
    ...


class LoteLogSchema(LoteLogBase):
    id: int
