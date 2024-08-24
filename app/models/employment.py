from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class Employment:
    __tablename__ = 'employment'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    farmer_id: Mapped[int] = mapped_column(ForeignKey('farmer.id'))
    farm_id: Mapped[int] = mapped_column(ForeignKey('farm.id'))
    employment_position_id: Mapped[int] = mapped_column(
        ForeignKey('employment_position.id')
    )


@table_registry.mapped_as_dataclass
class EmploymentPosition:
    __tablename__ = 'employment_position'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
