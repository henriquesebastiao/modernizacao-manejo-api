from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, DateTime, Integer, String

from app.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(40), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    phone: Mapped[str] = mapped_column(String(24))
    email: Mapped[str] = mapped_column(String(60), nullable=False)
    password: Mapped[str] = mapped_column(String(60))
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    update_at: Mapped[datetime] = mapped_column(DateTime,
                                                default=datetime.now())
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    type_id: Mapped[int] = mapped_column(ForeignKey('user_type.id'))
    manager_id: Mapped[int | None] = mapped_column(ForeignKey('user.id'),
                                                   nullable=True)
