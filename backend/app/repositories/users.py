from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.users import Users


def create_user(db: Session, user: Users) -> Users:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_by_username(db: Session, username: str) -> Users | None:
    query = select(Users).where(Users.username == username)
    
    return db.execute(query).scalar_one_or_none()