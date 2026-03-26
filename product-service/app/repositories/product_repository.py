from app.db.connection import mongo_connection


class ProductRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["products"]

    def get_all_products(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_product_by_id(self, product_id: int):
        return self.collection.find_one({"id": product_id}, {"_id": 0})

    def add_product(self, product: dict):
        self.collection.insert_one(product)
        return product

    def update_product(self, product_id: int, updated_product: dict):
        updated_product["id"] = product_id

        result = self.collection.update_one(
            {"id": product_id},
            {"$set": updated_product}
        )

        if result.matched_count == 0:
            return None

        return self.get_product_by_id(product_id)

    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)

        if not product:
            return None

        self.collection.delete_one({"id": product_id})
        return product