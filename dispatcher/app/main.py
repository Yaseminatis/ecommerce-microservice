import requests
from fastapi import FastAPI, Request

app = FastAPI(title="Dispatcher Service")

AUTH_SERVICE_URL = "http://localhost:8001"
USER_SERVICE_URL = "http://localhost:8002"
PRODUCT_SERVICE_URL = "http://localhost:8003"


@app.get("/")
def root():
    return {"message": "Dispatcher service is running"}


@app.post("/login")
async def login(request: Request):
    body = await request.json()
    response = requests.post(f"{AUTH_SERVICE_URL}/login", json=body)
    return response.json()


@app.get("/users")
def get_users():
    response = requests.get(f"{USER_SERVICE_URL}/users")
    return response.json()


@app.get("/products")
def get_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    return response.json()