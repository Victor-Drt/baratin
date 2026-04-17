from sqlalchemy.orm import Session
from ..schemas.users import CreateUserRequest, UserDetailResponse
from ..models.users import Users
from ..core.security import hash_password
from ..repositories import users as repository


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: CreateUserRequest) -> UserDetailResponse:
        user = Users(
            username=user_data.username,
            email=user_data.email,
            password_hash=hash_password(user_data.password)
        )
        
        new_user = repository.create_user(self.db, user)
        
        if not new_user:
            raise ValueError("Não foi possivel criar novo usuario")
        
        return new_user
    
    def get_user_by_username(self, username: str) -> Users:
        user = repository.get_by_username(self.db, username)
        
        return UserDetailResponse.model_validate(user)