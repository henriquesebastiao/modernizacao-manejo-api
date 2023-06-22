from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, String

from app.models.base import Base


class UserType(Base):
    __tablename__ = 'user_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
