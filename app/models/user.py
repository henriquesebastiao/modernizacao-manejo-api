from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, String

from app.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=False)
    password: Mapped[str] = mapped_column(String(60))
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[Optional[str]] = mapped_column(String(20))
    phone: Mapped[str] = mapped_column(String(24))


class UserType(Base):
    __tablename__ = 'user_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
