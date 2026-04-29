from fastapi.testclient import TestClient

from books_online.api import app
from books_online.products.service import delete_test_products

client = TestClient(app)


def test_get_products_all():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/products/all", headers=headers)
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_products_all_unauthorized():
    token = "wrongtoken"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/products/all", headers=headers)
    assert response.status_code == 403
    assert response.json().get("detail") == "Unauthorized"

def test_get_product_by_id():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/products/1", headers=headers)
    assert response.status_code == 200
    assert "product" in response.json()

def test_get_product_by_id_not_found():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/products/999", headers=headers)
    assert response.status_code == 404
    assert response.json().get("detail") == "Product not found"

def test_products_add():
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/products/add",
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 9.99,
            "inventory": 100
        },
        headers=headers
    )
    assert response.status_code == 200
    assert "message" in response.json()
    assert "product_id" in response.json()
    delete_test_products()

def test_products_add_unauthorized():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/products/add",
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 9.99,
            "inventory": 100
        },
        headers=headers
    )
    assert response.status_code == 403

def test_products_add_inventory():
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/products/add",
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 9.99,
            "inventory": 100
        },
        headers=headers
    )
    assert response.status_code == 200

    response_inventory = client.post(
        "/products/add_inventory",
        json={
            "product_id": 0,
            "quantity": 50
        },
        headers=headers
    )

    assert response_inventory.status_code == 200
    delete_test_products()
