from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from ....db.session import get_db
from ....schemas.users import UserDetailResponse
from ....schemas.categories import CategoryResponse
from ..deps import get_current_active_user
from ....services.categories import CategoryService


router = APIRouter()


@router.get("/",  response_model=list[CategoryResponse])
def get_categorys(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    service = CategoryService(db)
    
    return service.get_categories()
