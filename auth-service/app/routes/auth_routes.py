from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest, LoginResponse, LoginData
from app.repositories.auth_repository import AuthRepository

router = APIRouter()
auth_repository = AuthRepository()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user = auth_repository.get_user_by_username(data.username)

    if user and user["password"] == data.password:
        return LoginResponse(
            status="success",
            message="Giriş başarılı",
            data=LoginData(
                username=user["username"],
                token="fake-jwt-token"
            ),
        )

    return LoginResponse(
        status="error",
        message="Kullanıcı adı veya şifre hatalı",
        data=None
    )