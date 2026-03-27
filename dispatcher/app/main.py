import requests
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.route_map import ROUTE_MAP
from app.core.logger import logger

app = FastAPI(title="Dispatcher Service")


class LoginRequest(BaseModel):
    username: str
    password: str


PUBLIC_PATHS = ["/login"]
VALID_TOKEN = "Bearer fake-jwt-token"


def is_public_path(path: str) -> bool:
    return path in PUBLIC_PATHS


def check_auth_header(request: Request):
    authorization = request.headers.get("Authorization")

    if not authorization:
        logger.error("Authorization header eksik")
        raise HTTPException(
            status_code=401,
            detail="Token bulunamadi"
        )

    if authorization != VALID_TOKEN:
        logger.error("Gecersiz token gonderildi")
        raise HTTPException(
            status_code=403,
            detail="Gecersiz token"
        )


def forward_request(service: str, path: str, method="GET", data=None):
    target_url = ROUTE_MAP[service]
    url = f"{target_url}/{path}"

    logger.info(f"Istek yonlendiriliyor -> servis: {service}, method: {method}, url: {url}")

    try:
        if method == "POST":
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)

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
    logger.info(f"Yanıt donuldu -> status_code: {response.status_code}, path: {request.url.path}")
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
    logger.info("/users endpointi cagrildi")
    check_auth_header(request)
    return forward_request("users", "users")


@app.get("/products")
def get_products(request: Request):
    logger.info("/products endpointi cagrildi")
    check_auth_header(request)
    return forward_request("products", "products")


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    logger.error(f"Bulunamayan path istendi: /{full_path}")
    raise HTTPException(status_code=404, detail="Path bulunamadi")