from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class FarmerPlan(Base):
    __tablename__ = 'farmer_plan'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    plan: Mapped[str] = mapped_column(String(20), nullable=False)
