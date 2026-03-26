from app.db.connection import mongo_connection


class AuthRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()

    def get_user_by_username(self, username: str):
        if username == "admin":
            return {
                "username": "admin",
                "password": "1234"
            }
        return None