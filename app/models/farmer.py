from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Farmer(Base):
    __tablename__ = 'farmer'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    farmer_plan_id: Mapped[int] = mapped_column(Integer,
                                                ForeignKey('farmer_plan.id'))
