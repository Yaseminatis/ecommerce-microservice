from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):

    if data.username == "admin" and data.password == "1234":
                return LoginResponse(
            status="success",
            message="Giriş başarılı",
            username=data.username,
            token="fake-jwt-token"
        )
       raise HTTPException(
        status_code=401,
        detail="Kullanıcı adı veya şifre hatalı"
    )
    