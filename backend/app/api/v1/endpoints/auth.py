from fastapi import APIRouter
from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ....schemas.users import UserDetailResponse
from ....schemas.auth import Token, LoginRequest
from ....core.security import create_access_token, verify_password
from ....services.auth import AuthService
from ....db.session import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/")
async def login_for_access_token(
    data: LoginRequest, db: Session = Depends(get_db)
) -> Token:
    
    service = AuthService(db)
    
    access_token = service.authenticate_user(data)

    return Token(access_token=access_token, token_type="bearer")
