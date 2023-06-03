from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class FazendaPessoa(Base):
    __tablename__ = 'fazenda_pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fazenda_id = Column(Integer, ForeignKey('fazenda.id'))
    pessoa_id = Column(Integer)

    fazenda = relationship("Fazenda")
