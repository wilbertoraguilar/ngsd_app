from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, MagicMock
from books_online.api import app
from books_online.orders.service import remove_order

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
    remove_order(response.json()['order_id'])

def test_get_order_by_id():
    response_user = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testuser"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response_new_order = client.post(
        "/orders/new", headers=headers)
    response = client.get("/orders/" + str(response_new_order.json()['order_id']), headers=headers)
    assert response.status_code == 200
    assert "order" in response.json()
    remove_order(response_new_order.json()['order_id'])



def test_change_order_status():
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response_new_order = client.post(
        "/orders/new", headers=headers)
    response = client.post("/orders/" + str(response_new_order.json()['order_id']) + "/update_status", headers=headers)
    assert response.status_code == 200
    remove_order(response_new_order.json()['order_id'])


@pytest.fixture
def mock_celery_delay():
    """Patch Celery's delay to run synchronously in tests."""
    with patch("books_online.orders.tasks.process_basket.delay") as mock_delay:
        mock_result = MagicMock()
        mock_result.id = "test-task-id"
        mock_result.get.return_value = True
        mock_delay.return_value = mock_result
        yield mock_delay

def test_add_products_to_order(mock_celery_delay):
    response_user = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    token = response_user.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response_new_order = client.post(
        "/orders/new", headers=headers)
    basket = {
                "basket": [
                {
                "product_id": 1,
                "quantity": 1
                },
                {
                "product_id" :2,
                "quantity": 1
                }
            ]
    }


    response = client.post("/orders/" + str(response_new_order.json()['order_id']) + "/add_products", json=basket, headers=headers)
    assert response.status_code == 200
    data = response.json()
    # mock_celery_delay.assert_called_once_with(response_new_order.json()['order_id'], basket)
