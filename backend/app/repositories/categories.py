from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.categories import Category


def get_categories(db: Session) -> list[Category]:
    query = select(Category)
    
    return db.execute(query).scalars().all()