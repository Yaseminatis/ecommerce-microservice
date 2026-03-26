from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginData(BaseModel):
    username: str
    token: str


class LoginResponse(BaseModel):
    status: str
    message: str
    data: Optional[LoginData]