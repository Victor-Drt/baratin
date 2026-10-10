from fastapi import APIRouter, Depends
from typing import Annotated
from ....db.session import get_db
from sqlalchemy.orm import Session
from ....schemas.prices import PriceCreateRequest, PriceResponse
from ....schemas.users import UserDetailResponse
from ..deps import get_current_active_user
from ....services.prices import PriceService

router = APIRouter()


class PriceParams:
    skip: int = 0
    limit: int = 10

@router.post("/", response_model=PriceResponse)
def create_price(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    data: PriceCreateRequest,
    db: Session = Depends(get_db),
):
    price_service = PriceService(db)
    price = price_service.create_price(current_user.id, data)
    return PriceResponse.model_validate(price)

@router.get("/", response_model=list[PriceResponse])
def get_prices(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    product_id: int,
    location_id: int | None = None,
    db: Session = Depends(get_db),
):
    price_service = PriceService(db)

    prices = price_service.get_prices(product_id, location_id)
    return [PriceResponse.model_validate(price) for price in prices]

@router.get("/my-prices", response_model=list[PriceResponse])
def get_my_prices(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    db: Session = Depends(get_db),
):
    price_service = PriceService(db)
    prices = price_service.get_prices_by_user(current_user.id)
    return [PriceResponse.model_validate(price) for price in prices]