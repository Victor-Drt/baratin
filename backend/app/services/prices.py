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
        product = product_service.find_or_create_by_alias(
            raw_name=data.product_name,
            normalized_name=normalized_name,
            brand_id=data.brand_id,
            category_id=data.category_id
        )


        # 4 - find or create Location
        location = location_repository.find_by_name_city_state(
            self.db, 
            data.location.name,
            data.location.city,
            data.location.state
        )

        if not location:
            location = Location(**data.location.model_dump())
            location = location_repository.create_location(self.db, location)


        # 5 - save price
        price_created = price_repository.create_price(
            self.db, user_id, product.id, location.id, data.price, data.collected_at, link=data.link
        )

        return price_created

    def get_prices(self, product_id: int, location_id: int | None):
        return price_repository.get_prices_by_product(self.db, product_id, location_id)

    def get_prices_by_user(self, user_id: int):
        return price_repository.get_prices_by_user(self.db, user_id)