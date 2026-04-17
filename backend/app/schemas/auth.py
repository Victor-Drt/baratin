from pydantic import BaseModel

class StatusResponse(BaseModel):
    message: str = "servidor está ok!"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class LoginRequest(BaseModel):
    username: str
    password: str
