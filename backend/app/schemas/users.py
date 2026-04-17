from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserDetailResponse(UserBase):
    id: int
    created_at: datetime


class CreateUserRequest(UserBase):
    password: str
