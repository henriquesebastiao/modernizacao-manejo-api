from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class Farmer:
    __tablename__ = 'farmer'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    farmer_plan_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('farmer_plan.id')
    )


@table_registry.mapped_as_dataclass
class FarmerPlan:
    __tablename__ = 'farmer_plan'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    plan: Mapped[str]
