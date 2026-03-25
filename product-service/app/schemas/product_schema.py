from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float


class ProductResponse(BaseModel):
    status: str
    message: str
    data: Product


class ProductListResponse(BaseModel):
    status: str
    message: str
    data: list[Product]