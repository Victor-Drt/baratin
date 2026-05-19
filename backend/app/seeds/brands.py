from sqlalchemy.orm import Session
from ..models import Brand


BRANDS = [
  "Brastemp",
  "Electrolux",
  "Consul",
  "Samsung",
  "LG",
  "Midea",
  "Continental",
  "Atlas",
  "Mondial",
  "Arno",
  "Philco",
  "Britânia",
  "Oster",
  "Cadence",
  "Kappesberg",
  "Henn",
  "Itatiaia",
  "Lopas",
  "Moval",
  "DJ Móveis",
  "Dalla Costa",
  "Politorno",
  "Todeschini",
  "Dell Anno",
  "Florense",
  "Bontempo",
  "Ornare",
  "Sierra",
  "Ortobom",
  "Castor",
  "Herval",
  "Emma",
  "Simmons",
  "Probel",
  "King Koil"
]

def seed_brands(db: Session):
    for name in BRANDS:
        exists = db.query(Brand).filter_by(name=name).first()

        if not exists:
            db.add(Brand(name=name))

    db.commit()
