from fastapi import APIRouter
from .endpoints.auth import router as auth_router
from .endpoints.users import router as user_router
from .endpoints.categories import router as category_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/token", tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["user"])
api_router.include_router(category_router, prefix="/categories", tags=["category"])