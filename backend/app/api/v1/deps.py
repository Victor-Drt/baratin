from ...core.config import SECRET_KEY, ALGORITHM
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from typing import Annotated
import jwt
from ...schemas.auth import TokenData
from ...schemas.users import UserDetailResponse
from ...models.users import Users
from ...repositories import users as user_repository
from sqlalchemy.orm import Session
from ...db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user_dict = user_repository.get_by_username(db, token_data.username)
    if user_dict is None:
        raise credentials_exception
    return UserDetailResponse(
        id=user_dict.id,
        username=user_dict.username,
        email=user_dict.email,
        created_at=user_dict.created_at
    )


async def get_current_active_user(
    current_user: Annotated[UserDetailResponse, Depends(get_current_user)],
):
    if not current_user:
        raise HTTPException(status_code=400, detail="Usuário inativo")
    return current_user
