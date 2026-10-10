from sqlalchemy.orm import Session
from ..repositories import products as product_repository
from ..models.products import Product


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_products(self):
        """Retorna lista de todos os produtos com aliases, category e brand."""
        return product_repository.get_products(self.db)

    def find_or_create_by_alias(
        self, 
        raw_name: str, 
        normalized_name: str,
        brand_id: int,
        category_id: int
    ) -> Product:
        """Busca produto por alias normalizado, cria se não existir"""
        product = product_repository.find_by_alias_name(self.db, normalized_name)
        
        if not product:
            product = product_repository.create_product(
                self.db, normalized_name, brand_id, category_id
            )
            product_repository.save_alias(
                self.db, raw_name, product.id, normalized_name
            )
        else:
            existing_alias = product_repository.find_alias_by_id_and_raw(
                self.db, product.id, raw_name
            )
            if not existing_alias:
                product_repository.save_alias(
                    self.db, raw_name, product.id, normalized_name
                )
        
        return product
