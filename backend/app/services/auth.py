from sqlalchemy.orm import Session
from ..repositories import users as repository
from fastapi import HTTPException, status
from datetime import timedelta
from fastapi import HTTPException, status
from ..core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ..core.security import create_access_token, verify_password
from sqlalchemy.orm import Session
from ..schemas.auth import LoginRequest, Token


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def authenticate_user(self, data: LoginRequest) -> Token:

        user = repository.get_by_username(self.db, data.username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário ou senha incorretos",
            )

        if not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário ou senha incorretos",
            )

        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        
        return access_token
