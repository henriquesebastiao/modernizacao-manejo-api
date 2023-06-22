from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AnimalWeightType(Base):
    __tablename__ = 'weight_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(Integer, nullable=False)
