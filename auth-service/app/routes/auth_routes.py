from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest, LoginResponse, LoginData

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "1234":
        return LoginResponse(
            status="success",
            message="Giriş başarılı",
            data=LoginData(
                username=data.username,
                token="fake-jwt-token"
            ),
        )

    return LoginResponse(
        status="error",
        message="Kullanıcı adı veya şifre hatalı",
        data=None
    )