from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Fazendeiro(Base):
    __tablename__ = 'fazendeiro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    fazendas = relationship("Fazenda", back_populates="fazendeiro")
