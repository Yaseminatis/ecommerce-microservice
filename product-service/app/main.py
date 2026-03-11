from fastapi import FastAPI
from app.routes.product_routes import router as product_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Product Service ayakta"}

app.include_router(product_router)