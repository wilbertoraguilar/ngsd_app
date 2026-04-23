from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

# Import routers
from books_online.auth.router import router as auth_router
from books_online.products.router import router as products_router
from books_online.orders.router import router as orders_router


# Include routers
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
async def read_root():
   return "Books Online API is running"

def start():
    uvicorn.run("books_online.api:app", host=os.getenv("BE_HOST"), port=int(os.getenv("BE_PORT")), reload=True) # type: ignore

if __name__ == "__main__":
    start()
