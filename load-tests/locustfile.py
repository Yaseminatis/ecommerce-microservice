from locust import HttpUser, task, between


class EcommerceUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.auth_headers = {
            "Authorization": "Bearer admin-token"
        }

    @task(2)
    def login(self):
        self.client.post(
            "/login",
            json={
                "username": "admin",
                "password": "1234"
            },
            name="POST /login"
        )

    @task(2)
    def get_users(self):
        self.client.get(
            "/users",
            headers=self.auth_headers,
            name="GET /users"
        )

    @task(3)
    def get_products(self):
        self.client.get(
            "/products",
            headers=self.auth_headers,
            name="GET /products"
        )