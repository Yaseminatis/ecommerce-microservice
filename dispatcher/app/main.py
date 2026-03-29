import requests
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.route_map import ROUTE_MAP
from app.core.logger import logger
from app.repositories.auth_repository import DispatcherAuthRepository
from app.repositories.log_repository import LogRepository
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Dispatcher Service")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class LoginRequest(BaseModel):
    username: str
    password: str


PUBLIC_PATHS = ["/login"]
log_repository = LogRepository()

def get_auth_repository():
    return DispatcherAuthRepository()


def is_public_path(path: str) -> bool:
    return path in PUBLIC_PATHS


def get_user_role(request: Request):
    authorization = request.headers.get("Authorization")

    if not authorization:
        logger.error("Authorization header eksik")
        raise HTTPException(
            status_code=401,
            detail="Token bulunamadi"
        )

    role = get_auth_repository().get_role_by_token(authorization)

    if not role:
        logger.error("Gecersiz token gonderildi")
        raise HTTPException(
            status_code=403,
            detail="Gecersiz token"
        )

    return role


def check_role_permission(role: str, path: str):
    if not get_auth_repository().has_permission(role, path):
        logger.error(f"Yetkisiz erisim denemesi -> rol: {role}, path: {path}")
        raise HTTPException(
            status_code=403,
            detail="Bu alana erisim yetkiniz yok"
        )


def forward_request(service: str, path: str, method="GET", data=None):
    target_url = ROUTE_MAP[service]
    url = f"{target_url}/{path}"

    logger.info(f"Istek yonlendiriliyor -> servis: {service}, method: {method}, url: {url}")

    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            logger.error(f"Desteklenmeyen HTTP metodu: {method}")
            raise HTTPException(
                status_code=405,
                detail="Desteklenmeyen HTTP metodu"
            )

        logger.info(f"Servisten yanit alindi -> servis: {service}, status_code: {response.status_code}")
        return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f"Hedef servise ulasilamadi -> servis: {service}, url: {url}")
        raise HTTPException(
            status_code=503,
            detail="Hedef servis su anda ulasilamiyor"
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Servisten gecersiz yanit alindi -> servis: {service}, hata: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail="Servisten gecersiz yanit alindi"
        )


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Gelen istek -> method: {request.method}, path: {request.url.path}")
    response = await call_next(request)
    logger.info(f"Yanit donuldu -> status_code: {response.status_code}, path: {request.url.path}")

    try:
        log_repository.add_log(
            method=request.method,
            path=request.url.path,
            status_code=response.status_code
        )
    except Exception as e:
        logger.error(f"Log MongoDB'ye kaydedilemedi: {str(e)}")

    return response

@app.get("/")
def root():
    logger.info("Root endpoint cagrildi")
    return {"message": "Dispatcher service is running"}


@app.post("/login")
def login(data: LoginRequest):
    logger.info(f"Login istegi alindi -> username: {data.username}")
    return forward_request("login", "login", "POST", data.model_dump())


@app.get("/users")
def get_users(request: Request):
    logger.info("/users GET endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/users")
    return forward_request("users", "users", "GET")


@app.post("/users")
async def add_user(request: Request):
    logger.info("/users POST endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/users")
    body = await request.json()
    return forward_request("users", "users", "POST", body)


@app.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    logger.info(f"/users/{user_id} GET endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/users")
    return forward_request("users", f"users/{user_id}", "GET")


@app.put("/users/{user_id}")
async def update_user(user_id: int, request: Request):
    logger.info(f"/users/{user_id} PUT endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/users")
    body = await request.json()
    return forward_request("users", f"users/{user_id}", "PUT", body)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, request: Request):
    logger.info(f"/users/{user_id} DELETE endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/users")
    return forward_request("users", f"users/{user_id}", "DELETE")


@app.get("/products")
def get_products(request: Request):
    logger.info("/products GET endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/products")
    return forward_request("products", "products", "GET")


@app.post("/products")
async def add_product(request: Request):
    logger.info("/products POST endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/products")
    body = await request.json()
    return forward_request("products", "products", "POST", body)


@app.get("/products/{product_id}")
def get_product(product_id: int, request: Request):
    logger.info(f"/products/{product_id} GET endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/products")
    return forward_request("products", f"products/{product_id}", "GET")


@app.put("/products/{product_id}")
async def update_product(product_id: int, request: Request):
    logger.info(f"/products/{product_id} PUT endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/products")
    body = await request.json()
    return forward_request("products", f"products/{product_id}", "PUT", body)


@app.delete("/products/{product_id}")
def delete_product(product_id: int, request: Request):
    logger.info(f"/products/{product_id} DELETE endpointi cagrildi")
    role = get_user_role(request)
    check_role_permission(role, "/products")
    return forward_request("products", f"products/{product_id}", "DELETE")

@app.get("/logs")
def get_logs():
    logger.info("/logs endpointi cagrildi")
    return {
        "status": "success",
        "message": "Loglar listelendi",
        "data": log_repository.get_logs()
    }
@app.get("/dashboard")
def dashboard():
    return FileResponse("app/static/dashboard.html")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    logger.error(f"Bulunamayan path istendi: /{full_path}")
    raise HTTPException(status_code=404, detail="Path bulunamadi")