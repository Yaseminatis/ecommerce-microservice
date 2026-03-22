from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginData(BaseModel):
    username: str
    token: str


class LoginResponse(BaseModel):
    status: str
    message: str
    data: LoginData
