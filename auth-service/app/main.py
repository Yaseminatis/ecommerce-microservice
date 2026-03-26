from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="Auth Service")

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Auth service çalışıyor",
        "data": {
            "service": "auth-service"
        }
    }