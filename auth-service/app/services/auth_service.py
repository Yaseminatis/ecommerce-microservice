from app.repositories.auth_repository import AuthRepository


class AuthService:
    def __init__(self):
        self.auth_repository = AuthRepository()

    def login(self, username: str, password: str):
        user = self.auth_repository.get_user_by_username(username)

        if not user:
            return None

        if user["password"] != password:
            return None

        return user