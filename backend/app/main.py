from fastapi import FastAPI
from .api.v1.router import api_router


app = FastAPI()


app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["root"])
def root():
    return {"message": f"servidor está ok!"}
