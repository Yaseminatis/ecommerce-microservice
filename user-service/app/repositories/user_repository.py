from app.db.connection import mongo_connection


class UserRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.users = [
            {"id": 1, "name": "Ali", "email": "ali@mail.com"},
            {"id": 2, "name": "Ayşe", "email": "ayse@mail.com"},
        ]

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def add_user(self, user: dict):
        self.users.append(user)
        return user

    def update_user(self, user_id: int, updated_user: dict):
        for index, user in enumerate(self.users):
            if user["id"] == user_id:
                updated_user["id"] = user_id
                self.users[index] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: int):
        for index, user in enumerate(self.users):
            if user["id"] == user_id:
                deleted_user = self.users.pop(index)
                return deleted_user
        return None