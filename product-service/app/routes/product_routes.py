from fastapi import APIRouter
from app.schemas.product_schema import ProductRequest, ProductResponse

router = APIRouter()

products = [
    {"id": 1, "name": "Laptop", "price": 25000},
    {"id": 2, "name": "Mouse", "price": 500}
]

@router.get("/products")
def get_products():
    return {
        "status": "success",
        "message": "Ürünler listelendi",
        "data": products
    }

@router.post("/products", response_model=ProductResponse)
def add_product(product: ProductRequest):
    products.append(product.model_dump())
    return ProductResponse(
    message="Ürün eklendi",
    product=product
)