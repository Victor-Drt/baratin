from fastapi import FastAPI
from .api.v1.router import api_router
from .schemas.auth import StatusResponse

app = FastAPI()


app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["root"], response_model=StatusResponse)
def root():
    return {"message": "servidor está ok!"}
