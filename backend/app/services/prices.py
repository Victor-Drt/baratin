from sqlalchemy.orm import Session
from ..core.normalization import normalize_product_name
from ..schemas.prices import PriceCreateRequest
from ..services.products import ProductService
from ..repositories import products as product_repository
from ..repositories import locations as location_repository
from ..repositories import prices as price_repository
from ..models.locations import Location


class PriceService:
    def __init__(self, db: Session):
        self.db = db

    def create_price(self, user_id: int, data: PriceCreateRequest):
        product_service = ProductService(self.db)

        # 1 - normalize product name
        normalized_name: str = normalize_product_name(data.product_name)

        # 2 - find or create Product
        product = product_repository.find_by_alias_name(self.db, normalized_name)

        if not product:
            product = product_service.create_product(
                normalized_name, data.brand_id, data.category_id
            )  # falta adicionar brand_id e category_id para criar produto

        # 3 - save product alias
        product_repository.save_alias(
            self.db, data.product_name, product.id, normalized_name
        )

        # 4 - find or create Location
        location = location_repository.find_by_name_city(self.db, data.location.city)

        if not location:
            location = Location(**data.location.model_dump())
            location = location_repository.create_location(self.db, location)

        # 5 - save price
        price_created = price_repository.create_price(
            self.db, user_id, product.id, location.id, data.price, data.collected_at
        )

        return price_created

    def get_prices(self, product_id: int, location_id: int):
        return price_repository.get_prices_by_product_location(self.db, product_id, location_id)