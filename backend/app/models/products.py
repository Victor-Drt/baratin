from ..db.base import Base
from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, func, Index
from sqlalchemy.orm import mapped_column, Mapped, relationship


from sqlalchemy import ForeignKey, String, DateTime, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255)) 
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))

    category: Mapped["Category"] = relationship(back_populates="products")
    brand: Mapped["Brand"] = relationship(back_populates="products")

    # Aliases
    aliases: Mapped[list["ProductAliases"]] = relationship(back_populates="product")
    prices: Mapped[list["Price"]] = relationship(back_populates="product")
    
    __table_args__ = (
        Index("idx_product_name", "name"),
        Index("idx_product_brand", "brand_id"), # Corrigido para a coluna real
    )

class ProductAliases(Base):
    __tablename__ = "product_aliases"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    raw_name: Mapped[str] = mapped_column(String, nullable=False)
    normalized_name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    product = relationship("Product", back_populates="aliases")

    __table_args__ = (
        Index('idx_normalized_name', 'normalized_name'),
    )
