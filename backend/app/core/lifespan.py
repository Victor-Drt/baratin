from fastapi import FastAPI
from contextlib import asynccontextmanager
from ..db.session import SessionLocal
from ..core.config import ENV
from ..seeds.categories import seed_categories
from ..seeds.brands import seed_brands

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()

    if ENV == "dev":
        seed_categories(db)
        seed_brands(db)

    yield

    db.close()