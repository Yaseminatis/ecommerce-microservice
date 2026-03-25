from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import Product, ProductResponse, ProductListResponse

router = APIRouter()

products = [
    {"id": 1, "name": "Laptop", "price": 25000},
    {"id": 2, "name": "Mouse", "price": 500},
]


@router.get("/products", response_model=ProductListResponse)
def get_products():
    return ProductListResponse(
        status="success",
        message="Ürünler listelendi",
        data=[Product(**product) for product in products],
    )


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return ProductResponse(
                status="success",
                message="Ürün bulundu",
                data=Product(**product),
            )
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            updated_data = updated_product.model_dump()
            updated_data["id"] = product_id
            products[index] = updated_data
            return ProductResponse(
                status="success",
                message="Ürün güncellendi",
                data=Product(**updated_data),
            )
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return ProductResponse(
                status="success",
                message="Ürün silindi",
                data=Product(**deleted_product),
            )
    raise HTTPException(status_code=404, detail="Ürün bulunamadı")


@router.post("/products", response_model=ProductResponse)
def add_product(product: Product):
    products.append(product.model_dump())
    return ProductResponse(
        status="success",
        message="Ürün eklendi",
        data=product,
    )