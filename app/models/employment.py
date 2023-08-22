from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Employment(Base):
    __tablename__ = 'employment'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    farmer_id: Mapped[int] = mapped_column(Integer, ForeignKey('farmer.id'))
    farm_id: Mapped[int] = mapped_column(Integer, ForeignKey('farm.id'))
    employment_position_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('employment_position.id')
    )
