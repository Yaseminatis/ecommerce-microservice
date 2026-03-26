from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import User, UserResponse, UserListResponse
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/users", response_model=UserListResponse)
def get_users():
    users = user_service.get_all_users()
    return UserListResponse(
        status="success",
        message="Kullanıcılar listelendi",
        data=[User(**user) for user in users],
    )


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")

    return UserResponse(
        status="success",
        message="Kullanıcı bulundu",
        data=User(**user),
    )


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: User):
    updated_data = user_service.update_user(user_id, updated_user.model_dump())

    if not updated_data:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")

    return UserResponse(
        status="success",
        message="Kullanıcı güncellendi",
        data=User(**updated_data),
    )


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    deleted_user = user_service.delete_user(user_id)

    if not deleted_user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")

    return UserResponse(
        status="success",
        message="Kullanıcı silindi",
        data=User(**deleted_user),
    )


@router.post("/users", response_model=UserResponse)
def add_user(user: User):
    new_user = user_service.add_user(user.model_dump())

    return UserResponse(
        status="success",
        message="Kullanıcı eklendi",
        data=User(**new_user),
    )
