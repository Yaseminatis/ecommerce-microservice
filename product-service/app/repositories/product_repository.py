from app.db.connection import mongo_connection


class ProductRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["products"]

        self._seed_products()

    def _seed_products(self):
        seed_products = [
            {"id": 1, "name": "Laptop", "price": 25000},
            {"id": 2, "name": "Mouse", "price": 500},
            {"id": 3, "name": "Keyboard", "price": 1500},
            {"id": 4, "name": "Monitor", "price": 7000},
            {"id": 5, "name": "Kulaklik", "price": 1200},
            {"id": 6, "name": "Webcam", "price": 900},
            {"id": 7, "name": "Tablet", "price": 15000},
            {"id": 8, "name": "USB Bellek", "price": 250},
            {"id": 9, "name": "Hoparlor", "price": 1800},
            {"id": 10, "name": "Harici Disk", "price": 3500},
        ]

        for product in seed_products:
            self.collection.update_one(
                {"id": product["id"]},
                {"$setOnInsert": product},
                upsert=True
            )

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