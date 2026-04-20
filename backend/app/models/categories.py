from ..db.base import Base
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
