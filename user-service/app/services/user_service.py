from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)

    def add_user(self, user: dict):
        return self.user_repository.add_user(user)

    def update_user(self, user_id: int, updated_user: dict):
        return self.user_repository.update_user(user_id, updated_user)

    def delete_user(self, user_id: int):
        return self.user_repository.delete_user(user_id)