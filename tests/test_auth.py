from fastapi.testclient import TestClient

from books_online.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_loginUser():
    response = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "admin"}
    )
    assert response.status_code == 200
    assert response.json().get("token") is not None

def test_loginInvalidUser():
    response = client.post(
        "/auth/login",
        json={"email": "wrong@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 400
    assert response.json().get("error") == "Invalid email or password"

def test_registerUser():
    response = client.post(
        "/auth/register",
        json={ "name": "Admin", "email": "admin@example.com", "password": "admin", "admin": True }
    )
    assert response.status_code == 400
    assert response.json().get("error") == "User with this email already exists"

def test_registerTestUser():
    response = client.post(
        "/auth/register",
        json={ "name": "Test User", "email": "testuser@example.com", "password": "testuser", "admin": False })
    try:
        assert response.status_code == 200
    except AssertionError:
        assert response.status_code == 400
        assert response.json().get("error") == "User with this email already exists"


