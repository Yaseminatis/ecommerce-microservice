from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, Mock
import requests

client = TestClient(app)


def test_dispatcher_root_calisiyor_mu():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Dispatcher service is running"}


@patch("app.main.requests.post")
def test_login_auth_servicee_gidiyor_mu(mock_post):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Login başarılı"}
    mock_post.return_value = mock_response

    response = client.post(
        "/login",
        json={"username": "admin", "password": "1234"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login başarılı"


@patch("app.main.requests.get")
def test_users_user_servicee_gidiyor_mu(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "users": [
            {"id": 1, "name": "Ali"},
            {"id": 2, "name": "Ayşe"}
        ]
    }
    mock_get.return_value = mock_response

    response = client.get(
        "/users",
        headers={"Authorization": "Bearer fake-jwt-token"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert len(data["users"]) == 2


@patch("app.main.requests.get")
def test_products_product_servicee_gidiyor_mu(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "products": [
            {"id": 1, "name": "Laptop", "price": 25000},
            {"id": 2, "name": "Mouse", "price": 500}
        ]
    }
    mock_get.return_value = mock_response

    response = client.get(
        "/products",
        headers={"Authorization": "Bearer fake-jwt-token"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert len(data["products"]) == 2


def test_bilinmeyen_path_404_donuyor_mu():
    response = client.get("/olmayan-path")
    assert response.status_code == 404
    assert response.json()["detail"] == "Path bulunamadi"


def test_users_token_yoksa_401_donuyor_mu():
    response = client.get("/users")

    assert response.status_code == 401
    assert response.json()["detail"] == "Token bulunamadi"


def test_products_token_yoksa_401_donuyor_mu():
    response = client.get("/products")

    assert response.status_code == 401
    assert response.json()["detail"] == "Token bulunamadi"


def test_users_token_yanlissa_403_donuyor_mu():
    response = client.get(
        "/users",
        headers={"Authorization": "Bearer yanlis-token"}
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Gecersiz token"


def test_products_token_yanlissa_403_donuyor_mu():
    response = client.get(
        "/products",
        headers={"Authorization": "Bearer yanlis-token"}
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Gecersiz token"


@patch("app.main.requests.get")
def test_user_service_kapaliyken_503_donuyor_mu(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Service down")

    response = client.get(
        "/users",
        headers={"Authorization": "Bearer fake-jwt-token"}
    )

    assert response.status_code == 503
    assert response.json()["detail"] == "Hedef servis su anda ulasilamiyor"


@patch("app.main.requests.get")
def test_product_service_kapaliyken_503_donuyor_mu(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Service down")

    response = client.get(
        "/products",
        headers={"Authorization": "Bearer fake-jwt-token"}
    )

    assert response.status_code == 503
    assert response.json()["detail"] == "Hedef servis su anda ulasilamiyor"