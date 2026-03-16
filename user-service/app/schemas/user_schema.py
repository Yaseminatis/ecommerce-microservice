from pydantic import BaseModel

class UserRequest(BaseModel):
    id: int
    name: str
    email: str


class UserResponse(BaseModel):
    message: str
    user: UserRequest