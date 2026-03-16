from fastapi import APIRouter
from app.schemas.user_schema import UserRequest, UserResponse

router = APIRouter()

users = [
    {"id": 1, "name": "Ali", "email": "ali@mail.com"},
    {"id": 2, "name": "Ayşe", "email": "ayse@mail.com"}
]


@router.get("/users")
def get_users():
    return {"users": users}


@router.post("/users", response_model=UserResponse)
def add_user(user: UserRequest):
    users.append(user.model_dump())
    return UserResponse(
        message="Kullanıcı eklendi",
        user=user
    )