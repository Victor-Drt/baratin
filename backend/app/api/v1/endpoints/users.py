from fastapi import APIRouter, Depends
from typing import Annotated

from ....schemas.users import CreateUserRequest, UserDetailResponse
from ..deps import get_current_active_user
from ....db.session import get_db
from sqlalchemy.orm import Session
from ....services.users import UserService


router = APIRouter()


@router.get("/me")
async def read_users_me(
    current_user: Annotated[UserDetailResponse, Depends(get_current_active_user)],
) -> UserDetailResponse:
    """
    Rota protegida que retorna os dados do usuário logado.
    """
    return current_user


@router.post("/", response_model=UserDetailResponse)
def create_user(user_data: CreateUserRequest, db: Session = Depends(get_db)) -> UserDetailResponse:
    service = UserService(db)
    return service.create_user(user_data)
