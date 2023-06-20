from sqlalchemy.ext.asyncio import AsyncSession

from app.models.pessoa import Pessoa
from app.repositories.base import BaseRepository
from app.schemas.pessoa import PessoaSchema


class PessoaRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Pessoa, PessoaSchema, db)
