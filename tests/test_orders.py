from fastapi.testclient import TestClient

from books_online.api import app
from books_online.products.service import delete_test_products

client = TestClient(app)


def test_get_orders_all():
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/orders/all", headers=headers)
    assert response.status_code == 200
    assert "orders" in response.json()


def test_orders_add():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/orders/new", headers=headers)
    assert response.status_code == 200


def test_get_order_by_id():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response_all = client.get("/orders/all", headers=headers)
    response = client.get("/orders/" + str(response_all.json()['orders'][0]['id']), headers=headers)
    assert response.status_code == 200
    assert "order" in response.json()


def test_change_order_status():
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response_all = client.get("/orders/all", headers=headers)
    response = client.post("/orders/" + str(response_all.json()['orders'][0]['id']) + "/update_status", headers=headers)
    assert response.status_code == 200
