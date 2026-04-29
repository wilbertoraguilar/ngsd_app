from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
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
    if user:
        return {"message": "Registeration successful", "user_id": user.id}
    else:
        return JSONResponse(
        content={"error": "User with this email already exists"},
        status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/auth/login")
async def user_login(data: dict):
    email = data.get("email")
    password = data.get("password")
    token = login(str(email), str(password))
    if token is None:
        return JSONResponse (
            content={"error": "Invalid email or password"},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"token": token}

