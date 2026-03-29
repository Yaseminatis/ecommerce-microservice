from app.db.connection import mongo_connection


class DispatcherAuthRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.tokens_collection = self.db["tokens"]
        self.permissions_collection = self.db["permissions"]

        self._seed_tokens()
        self._seed_permissions()

    def _seed_tokens(self):
        seed_tokens = [
            {"token": "Bearer admin-token", "role": "admin"},
            {"token": "Bearer user-token", "role": "user"},
        ]

        for item in seed_tokens:
            self.tokens_collection.update_one(
                {"token": item["token"]},
                {"$setOnInsert": item},
                upsert=True
            )

    def _seed_permissions(self):
        seed_permissions = [
            {"role": "admin", "path": "/users"},
            {"role": "admin", "path": "/products"},
            {"role": "user", "path": "/products"},
        ]

        for item in seed_permissions:
            self.permissions_collection.update_one(
                {"role": item["role"], "path": item["path"]},
                {"$setOnInsert": item},
                upsert=True
            )

    def get_role_by_token(self, token: str):
        token_data = self.tokens_collection.find_one(
            {"token": token},
            {"_id": 0}
        )
        if not token_data:
            return None
        return token_data["role"]

    def has_permission(self, role: str, path: str):
        permission = self.permissions_collection.find_one(
            {"role": role, "path": path},
            {"_id": 0}
        )
        return permission is not None