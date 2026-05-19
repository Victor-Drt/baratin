from pydantic import BaseModel, ConfigDict
from ..schemas.locations import LocationCreateRequest
from datetime import datetime


class PriceCreateRequest(BaseModel):
    product_name: str
    price: float
    collected_at: datetime 
    brand_id: int
    category_id: int
    location: LocationCreateRequest


class PriceResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    location_id: int
    price: float
    currency: str
    collected_at: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
