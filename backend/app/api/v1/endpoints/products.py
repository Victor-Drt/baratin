from fastapi import APIRouter, Depends
from typing import Annotated
from ....schemas.users import UserDetailResponse
from ....schemas.products import ProductResponse
from ..deps import get_current_active_user
from ....db.session import get_db
from sqlalchemy.orm import Session
from ....services.products import ProductService
from ....models.users import Users


router = APIRouter()


@router.get("/", response_model=list[ProductResponse])
def get_products(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    return service.get_products()
