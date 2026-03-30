from fastapi import FastAPI
from app.routes.product_routes import router as product_router

app = FastAPI(title="Product Service")

app.include_router(product_router)


@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Product service çalışıyor",
        "data": {"service": "product-service"},
    }
