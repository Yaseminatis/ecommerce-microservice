from app.db.connection import mongo_connection


class AuthRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["users"]

        self._seed_users()

    def _seed_users(self):
        seed_users = [
            {"username": "admin", "password": "1234"},
            {"username": "yasemin", "password": "1234"},
            {"username": "senay", "password": "1234"},
            {"username": "ali", "password": "1234"},
            {"username": "ayse", "password": "1234"},
            {"username": "mehmet", "password": "1234"},
            {"username": "zeynep", "password": "1234"},
        ]

        for user in seed_users:
            self.collection.update_one(
                {"username": user["username"]},
                {"$setOnInsert": user},
                upsert=True
            )

    def get_user_by_username(self, username: str):
        return self.collection.find_one(
            {"username": username},
            {"_id": 0}
        )