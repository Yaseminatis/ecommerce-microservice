from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_all_products()

    def get_product_by_id(self, product_id: int):
        return self.product_repository.get_product_by_id(product_id)

    def add_product(self, product: dict):
        return self.product_repository.add_product(product)

    def update_product(self, product_id: int, updated_product: dict):
        return self.product_repository.update_product(product_id, updated_product)

    def delete_product(self, product_id: int):
        return self.product_repository.delete_product(product_id)