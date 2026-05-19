from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.locations import Location

def find_by_name_city(db: Session, city: str) -> Location | None:
    stmt = (
        select(Location).where(Location.city == city)
    )
    return db.execute(stmt).scalar_one_or_none()

def create_location(db: Session, location: Location):
    db.add(location)
    db.commit()
    db.refresh(location)
    return location