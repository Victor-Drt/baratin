from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from ..db.base import Base


class Users(Base):
    __tablename__ = "users"    
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
