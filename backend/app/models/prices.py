from ..db.base import Base
from sqlalchemy import String, DateTime, Numeric, Integer, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from decimal import Decimal


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))

    link: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    currency: Mapped[str] = mapped_column(String(3), default="brl")
    collected_at: Mapped[datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    product: Mapped["Product"] = relationship(back_populates="prices")
    user: Mapped["Users"] = relationship(back_populates="prices")
    location: Mapped["Location"] = relationship(back_populates="prices")
