from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    phone: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(default=datetime.now())
    update_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )
    active: Mapped[bool] = mapped_column(default=True)

    user_type_id: Mapped[int] = mapped_column(
        ForeignKey('user_type.id'), default=1
    )
    manager_id: Mapped[int | None] = mapped_column(
        ForeignKey('user.id'), nullable=True, default=1
    )


@table_registry.mapped_as_dataclass
class UserType:
    __tablename__ = 'user_type'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[str]
