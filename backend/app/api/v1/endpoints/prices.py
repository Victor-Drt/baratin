from fastapi import APIRouter, Depends
from typing import Annotated
from ....db.session import get_db
from sqlalchemy.orm import Session
from ....schemas.prices import PriceCreateRequest, PriceResponse
from ....schemas.users import UserDetailResponse
from ..deps import get_current_active_user
from ....services.prices import PriceService

router = APIRouter()


@router.post("/")
def create_price(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    data: PriceCreateRequest,
    db: Session = Depends(get_db),
):
    price_service = PriceService(db)
    return price_service.create_price(current_user.id, data)

@router.get("/", response_model=list[PriceResponse])
def get_prices(
    product_id: int,
    location_id: int,
    db: Session = Depends(get_db),
):
    price_service = PriceService(db)
    return price_service.get_prices(product_id, location_id)