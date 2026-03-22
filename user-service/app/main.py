from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI(title="User Service")


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "User service çalışıyor",
        "data": {"service": "user-service"},
    }


app.include_router(user_router)
