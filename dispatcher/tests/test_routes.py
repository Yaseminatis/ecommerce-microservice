from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_login_auth_servicee_gidiyor_mu():
    with patch("app.main.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "auth response"}

        response = client.post("/login", json={"username": "test", "password": "1234"})

        assert response.status_code == 200
        mock_post.assert_called_once()


def test_users_user_servicee_gidiyor_mu():
    with patch("app.main.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "name": "Yasemin"}]

        response = client.get("/users")

        assert response.status_code == 200
        mock_get.assert_called_once()


def test_products_product_servicee_gidiyor_mu():
    with patch("app.main.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "name": "Kalem"}]

        response = client.get("/products")

        assert response.status_code == 200
        mock_get.assert_called_once()