from fastapi import APIRouter, Depends
from typing import Annotated

from ....schemas.users import User
from ..deps import get_current_active_user


router = APIRouter()


@router.get("/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """
    Rota protegida que retorna os dados do usuário logado.
    """
    return current_user