from app.db.connection import mongo_connection


class UserRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["users"]

        self._migrate_legacy_users()
        self._seed_users()

    def _migrate_legacy_users(self):
        users = list(self.collection.find({}))

        for user in users:
            update_data = {}

            if "name" not in user and "username" in user:
                update_data["name"] = user["username"].capitalize()

            if "email" not in user:
                if "username" in user:
                    update_data["email"] = f'{user["username"]}@test.com'
                elif "name" in user:
                    update_data["email"] = f'{user["name"].lower()}@test.com'

            if update_data:
                self.collection.update_one(
                    {"_id": user["_id"]},
                    {"$set": update_data}
                )

    def _seed_users(self):
        seed_users = [
            {"id": 1, "name": "Admin", "email": "admin@test.com"},
            {"id": 2, "name": "Yasemin", "email": "yasemin@test.com"},
            {"id": 3, "name": "Senay", "email": "senay@test.com"},
            {"id": 4, "name": "Ali", "email": "ali@test.com"},
            {"id": 5, "name": "Ayse", "email": "ayse@test.com"},
            {"id": 6, "name": "Mehmet", "email": "mehmet@test.com"},
            {"id": 7, "name": "Zeynep", "email": "zeynep@test.com"},
        ]

        for user in seed_users:
            self.collection.update_one(
                {"id": user["id"]},
                {"$setOnInsert": user},
                upsert=True
            )

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