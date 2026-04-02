from fastapi import APIRouter
from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ....schemas.users import UserInDB
from ....schemas.auth import Token, LoginRequest
from ....db.session import fake_users_db
from ....core.security import create_access_token, verify_password


router = APIRouter()


@router.post("/")
async def login_for_access_token(
    data: LoginRequest,
) -> Token:
    user_dict = fake_users_db.get(data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
        )

    user = UserInDB(**user_dict)

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
        )

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")