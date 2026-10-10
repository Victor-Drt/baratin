# criar produto
# buscar produto
from sqlalchemy import select, literal, func
from sqlalchemy.orm import Session, joinedload
from ..models.products import Product, ProductAliases


def get_products(db: Session) -> list[Product]:
    """Retorna todos os produtos com aliases, category e brand carregados."""
    stmt = (
        select(Product)
        .options(
            joinedload(Product.aliases),
            joinedload(Product.category),
            joinedload(Product.brand)
        )
    )
    return db.execute(stmt).unique().scalars().all()

def find_by_alias_name(db: Session, normalized_name: str) -> Product | None:
    stmt = (
        select(Product)
        .join(ProductAliases, ProductAliases.product_id == Product.id)
        .where(ProductAliases.normalized_name == normalized_name)
        .limit(1)
    )

    return db.execute(stmt).scalar_one_or_none()


def create_product(db: Session, normalized_name: str, brand_id: int, category_id: int) -> Product:
    new_product = Product(name=normalized_name, brand_id=brand_id, category_id=category_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def find_alias_by_id_and_raw(db: Session, product_id: int, raw_name: str) -> ProductAliases | None:
    stmt = select(ProductAliases).where(
        (ProductAliases.product_id == product_id) &
        (ProductAliases.raw_name == raw_name)
    )
    return db.execute(stmt).scalar_one_or_none()


def save_alias(db: Session, raw_name: str, product_id: int, normalized_name: str):
    new_alias = ProductAliases(
        product_id=product_id,
        raw_name=raw_name,
        normalized_name=normalized_name
    )
    db.add(new_alias)
    db.commit()
    db.refresh(new_alias)
    return new_alias
