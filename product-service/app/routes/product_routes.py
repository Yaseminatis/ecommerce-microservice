from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import Product, ProductResponse, ProductListResponse
from app.repositories.product_repository import ProductRepository

router = APIRouter()
product_repository = ProductRepository()


@router.get("/products", response_model=ProductListResponse)
def get_products():
    products = product_repository.get_all_products()
    return ProductListResponse(
        status="success",
        message="Ürünler listelendi",
        data=[Product(**product) for product in products],
    )


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    product = product_repository.get_product_by_id(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")

    return ProductResponse(
        status="success",
        message="Ürün bulundu",
        data=Product(**product),
    )


@router.post("/products", response_model=ProductResponse)
def add_product(product: Product):
    new_product = product_repository.add_product(product.model_dump())

    return ProductResponse(
        status="success",
        message="Ürün eklendi",
        data=Product(**new_product),
    )


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, updated_product: Product):
    updated_data = product_repository.update_product(
        product_id, updated_product.model_dump()
    )

    if not updated_data:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")

    return ProductResponse(
        status="success",
        message="Ürün güncellendi",
        data=Product(**updated_data),
    )


@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int):
    deleted_product = product_repository.delete_product(product_id)

    if not deleted_product:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")

    return ProductResponse(
        status="success",
        message="Ürün silindi",
        data=Product(**deleted_product),
    )