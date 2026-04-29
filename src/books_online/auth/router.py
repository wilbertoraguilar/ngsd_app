from fastapi import APIRouter
from books_online.auth.service import login, register

router = APIRouter()


@router.post("/auth/register")
async def register_user(data: dict):
    user = register(
        name=str(data.get("name")),
        email=str(data.get("email")),
        password=str(data.get("password")),
        admin=data.get("admin", False),
    )
    return {"message": "Registeration successful", "user_id": user.id}


@router.post("/auth/login")
async def user_login(data: dict):
    email = data.get("email")
    password = data.get("password")
    token = login(str(email), str(password))
    if token is None:
        return {"error": "Invalid email or password"}
    return {"token": token}
