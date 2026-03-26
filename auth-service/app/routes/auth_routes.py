from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest, LoginResponse, LoginData
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user = auth_service.login(data.username, data.password)

    if user:
        return LoginResponse(
            status="success",
            message="Giriş başarılı",
            data=LoginData(username=user["username"], token="fake-jwt-token"),
        )

    return LoginResponse(
        status="error", message="Kullanıcı adı veya şifre hatalı", data=None
    )
