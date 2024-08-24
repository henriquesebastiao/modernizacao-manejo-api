from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class Farm:
    __tablename__ = 'farm'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
