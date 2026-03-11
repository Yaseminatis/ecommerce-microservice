from fastapi import APIRouter

router = APIRouter()

users = [
    {"id": 1, "name": "Ali", "email": "ali@example.com"},
    {"id": 2, "name": "Ayşe", "email": "ayse@example.com"}
]

@router.get("/users")
def get_users():
    return {"users": users}

@router.post("/users")
def add_user(user: dict):
    users.append(user)
    return {
        "message": "Kullanıcı eklendi",
        "user": user
    }