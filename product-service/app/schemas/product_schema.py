from pydantic import BaseModel

class ProductRequest(BaseModel):
    id: int
    name: str
    price: float


class ProductResponse(BaseModel):
    message: str
    product: ProductRequest