from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = Column(String)
    password: Mapped[str] = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))

    pessoa = relationship("Pessoa")
