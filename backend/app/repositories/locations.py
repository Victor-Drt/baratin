from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.locations import Location


def find_by_name_city_state(db: Session, name: str, city: str, state: str) -> Location | None:
    stmt = select(Location).where(
        (Location.name == name) &
        (Location.city == city) &
        (Location.state == state)
    )
    return db.execute(stmt).scalar_one_or_none()


def create_location(db: Session, location: Location):
    db.add(location)
    db.commit()
    db.refresh(location)
    return location
