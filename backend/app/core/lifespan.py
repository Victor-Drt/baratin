from fastapi import FastAPI
from contextlib import asynccontextmanager
from ..db.session import SessionLocal
from ..core.config import ENV
from ..seeds.categories import seed_categories

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()

    if ENV == "dev":
        seed_categories(db)

    yield

    db.close()