import requests
from fastapi import FastAPI
from pydantic import BaseModel
from app.route_map import ROUTE_MAP

app = FastAPI(title="Dispatcher Service")


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def root():
    return {"message": "Dispatcher service is running"}


@app.post("/login")
def login(data: LoginRequest):
    target_url = ROUTE_MAP["login"]
    response = requests.post(f"{target_url}/login", json=data.model_dump())
    return response.json()


@app.get("/users")
def get_users():
    target_url = ROUTE_MAP["users"]
    response = requests.get(f"{target_url}/users")
    return response.json()


@app.get("/products")
def get_products():
    target_url = ROUTE_MAP["products"]
    response = requests.get(f"{target_url}/products")
    return response.json()