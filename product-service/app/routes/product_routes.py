from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import ProductRequest, ProductResponse

router = APIRouter()

products = [
    {"id": 1, "name": "Laptop", "price": 25000},
    {"id": 2, "name": "Mouse", "price": 500},
]


@router.get("/products")
def get_products():
    return {"status": "success", "message": "Ürünler listelendi", "data": products}


@router.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"status": "success", "message": "Ürün bulundu", "data": product}
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: dict):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            updated_product["id"] = product_id
            products[index] = updated_product
            return {
                "status": "success",
                "message": "Ürün güncellendi",
                "data": updated_product,
            }
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return {
                "status": "success",
                "message": "Ürün silindi",
                "data": deleted_product,
            }
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.post("/products", response_model=ProductResponse)
def add_product(product: ProductRequest):
    products.append(product.model_dump())
    return ProductResponse(status="success", message="Ürün eklendi", data=product)
