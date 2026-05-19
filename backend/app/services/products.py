from sqlalchemy.orm import Session
from ..repositories import products as product_repository


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, normalized_name: str, brand_id: int, category_id: int):
        product = product_repository.create_product(self.db, normalized_name, brand_id, category_id)
        return product