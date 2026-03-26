from app.db.connection import mongo_connection


class ProductRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.products = [
            {"id": 1, "name": "Laptop", "price": 25000},
            {"id": 2, "name": "Mouse", "price": 500},
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id: int):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def add_product(self, product: dict):
        self.products.append(product)
        return product

    def update_product(self, product_id: int, updated_product: dict):
        for index, product in enumerate(self.products):
            if product["id"] == product_id:
                updated_product["id"] = product_id
                self.products[index] = updated_product
                return updated_product
        return None

    def delete_product(self, product_id: int):
        for index, product in enumerate(self.products):
            if product["id"] == product_id:
                deleted_product = self.products.pop(index)
                return deleted_product
        return None