from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.prices import Price
from datetime import datetime


def create_price(
    db: Session, user_id: int,  product_id: int, location_id: int, price: float, collected_at: datetime, link: str
):
    new_price = Price(
        product_id=product_id,
        location_id=location_id,
        price=price,
        collected_at=collected_at,
        user_id=user_id,
        link=link
    )
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    return new_price


def get_prices_by_product_location(db: Session, product_id: int, location_id: int):
    stmt = select(Price).where(Price.product_id == product_id, Price.location_id == location_id)
    return db.execute(stmt).scalars().all()

def get_prices_by_product(db: Session, product_id: int, location_id: int | None):

    if location_id is not None:
        stmt = select(Price).where(
            Price.product_id == product_id,
            Price.location_id == location_id
        )
    else:
        stmt = select(Price).where(
            Price.product_id == product_id
        )

    return db.execute(stmt).scalars().all()


def get_prices_by_user(db: Session, user_id: int):
    stmt = select(Price).where(Price.user_id == user_id)
    return db.execute(stmt).scalars().all()
