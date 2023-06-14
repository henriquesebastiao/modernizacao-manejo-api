from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Fazendeiro(Base):
    __tablename__ = 'fazendeiro'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    fazenda = relationship("Fazenda", back_populates="fazendeiro")
