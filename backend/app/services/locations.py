from sqlalchemy.orm import Session
from ..repositories import locations as repository


class LocationService:
    
    def __init__(self, db: Session):
        self.db = db
        
    def create_location(self):
        location = repository.create_location(self.db)
        return location