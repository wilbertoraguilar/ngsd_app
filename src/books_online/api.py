from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

from books_online.auth.utils import is_token_user_admin, is_token_valid

app = FastAPI()
load_dotenv()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://books_online_frontend",
    "http://books_online_frontend:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Import routers
from books_online.auth.router import router as auth_router
from books_online.products.router import router as products_router
from books_online.orders.router import router as orders_router


# Include routers
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(orders_router)

NO_AUTH_PATHS = ["/", "/auth/login", "/auth/register"]
ADMIN_PATHS = ["/products/add", "/products/add_inventory"]


@app.middleware("http")
async def is_authenticated(request: Request, call_next):
    if (
        not is_token_valid(request.headers.get("Authorization", ""))
        and request.url.path not in NO_AUTH_PATHS
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Unauthorized"}
        )
    response = await call_next(request)
    return response


@app.middleware("http")
async def is_admin(request: Request, call_next):
    if (
        not is_token_valid(request.headers.get("Authorization", ""))
        and request.url.path not in NO_AUTH_PATHS
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Unauthorized"}
        )
    if (
        not is_token_user_admin(request.headers.get("Authorization", ""))
        and request.url.path in ADMIN_PATHS
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Unauthorized"}
        )
    response = await call_next(request)
    return response


@app.get("/")
async def read_root():
    return "Books Online API is running"


def start():
    uvicorn.run("books_online.api:app", host=os.getenv("BE_HOST"), port=int(os.getenv("BE_PORT")), reload=True)  # type: ignore


if __name__ == "__main__":
    start()
