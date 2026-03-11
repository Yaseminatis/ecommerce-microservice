from fastapi import APIRouter

router = APIRouter()

products = [
    {"id": 1, "name": "Laptop", "price": 25000},
    {"id": 2, "name": "Mouse", "price": 500}
]

@router.get("/products")
def get_products():
    return {"products": products}

@router.post("/products")
def add_product(product: dict):
    products.append(product)
    return {"message": "Ürün eklendi", "product": product}