from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Batch(Base):
    __tablename__ = "batch"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    reg: Mapped[str] = mapped_column(String(20), nullable=False)
    farm_id: Mapped[int] = mapped_column(Integer, ForeignKey('farm.id'))
