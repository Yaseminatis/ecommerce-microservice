from app.db.connection import mongo_connection


class UserRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["users"]

    def get_all_users(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_user_by_id(self, user_id: int):
        return self.collection.find_one({"id": user_id}, {"_id": 0})

    def add_user(self, user: dict):
        self.collection.insert_one(user)
        return user

    def update_user(self, user_id: int, updated_user: dict):
        updated_user["id"] = user_id

        result = self.collection.update_one(
            {"id": user_id},
            {"$set": updated_user}
        )

        if result.matched_count == 0:
            return None

        return self.get_user_by_id(user_id)

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)

        if not user:
            return None

        self.collection.delete_one({"id": user_id})
        return user