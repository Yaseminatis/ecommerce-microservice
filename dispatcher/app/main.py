import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.route_map import ROUTE_MAP

app = FastAPI(title="Dispatcher Service")


class LoginRequest(BaseModel):
    username: str
    password: str


def forward_request(service: str, path: str, method="GET", data=None):
    target_url = ROUTE_MAP[service]
    url = f"{target_url}/{path}"

    try:
        if method == "POST":
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)

        return response.json()

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Hedef servis su anda ulasilamiyor"
        )
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Servisten gecersiz yanit alindi"
        )


@app.get("/")
def root():
    return {"message": "Dispatcher service is running"}


@app.post("/login")
def login(data: LoginRequest):
    return forward_request("login", "login", "POST", data.model_dump())


@app.get("/users")
def get_users():
    return forward_request("users", "users")


@app.get("/products")
def get_products():
    return forward_request("products", "products")


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    raise HTTPException(status_code=404, detail="Path bulunamadi")