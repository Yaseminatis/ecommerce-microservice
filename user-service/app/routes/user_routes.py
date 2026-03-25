from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import User, UserResponse, UserListResponse

router = APIRouter()

users = [
    {"id": 1, "name": "Ali", "email": "ali@mail.com"},
    {"id": 2, "name": "Ayşe", "email": "ayse@mail.com"},
]


@router.get("/users", response_model=UserListResponse)
def get_users():
    return UserListResponse(
        status="success",
        message="Kullanıcılar listelendi",
        data=[User(**user) for user in users],
    )


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return UserResponse(
                status="success",
                message="Kullanıcı bulundu",
                data=User(**user),
            )
    raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            updated_data = updated_user.model_dump()
            updated_data["id"] = user_id
            users[index] = updated_data
            return UserResponse(
                status="success",
                message="Kullanıcı güncellendi",
                data=User(**updated_data),
            )
    raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)
            return UserResponse(
                status="success",
                message="Kullanıcı silindi",
                data=User(**deleted_user),
            )
    raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")


@router.post("/users", response_model=UserResponse)
def add_user(user: User):
    users.append(user.model_dump())
    return UserResponse(
        status="success",
        message="Kullanıcı eklendi",
        data=user,
    )