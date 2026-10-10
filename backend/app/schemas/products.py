from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProductAliasResponse(BaseModel):
    id: int
    raw_name: str
    normalized_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BrandResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductResponse(BaseModel):
    id: int
    name: str
    category_id: int
    brand_id: int
    created_at: datetime
    aliases: list[ProductAliasResponse]
    category: CategoryResponse
    brand: BrandResponse

    model_config = ConfigDict(from_attributes=True)
