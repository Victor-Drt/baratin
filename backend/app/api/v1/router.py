from fastapi import APIRouter
from .endpoints.auth import router as auth_router
from .endpoints.users import router as user_router
from .endpoints.categories import router as category_router
from .endpoints.prices import router as price_router
from .endpoints.products import router as product_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/token", tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["user"])
api_router.include_router(category_router, prefix="/categories", tags=["category"])
api_router.include_router(price_router, prefix="/prices", tags=["price"])
api_router.include_router(product_router, prefix="/products", tags=["product"])

