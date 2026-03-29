from app.db.connection import mongo_connection


class AuthRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["users"]

        if self.collection.count_documents({}) == 0:
            self.collection.insert_one({
                "username": "admin",
                "password": "1234"
            })

    def get_user_by_username(self, username: str):
        return self.collection.find_one(
            {"username": username},
            {"_id": 0}
        )