from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class UserResponse(BaseModel):
    status: str
    message: str
    data: User


class UserListResponse(BaseModel):
    status: str
    message: str
    data: list[User]