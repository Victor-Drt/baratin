from sqlalchemy.orm import Session
from ..models import Category

CATEGORIES = [
    "eletrodomestico",
    "moveis",
    "eletronicos",
    "cozinha",
    "quarto"
]

def seed_categories(db: Session):
    for name in CATEGORIES:
        exists = db.query(Category).filter_by(name=name).first()

        if not exists:
            db.add(Category(name=name))

    db.commit()
