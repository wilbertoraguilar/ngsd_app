

from fastapi import APIRouter, Request
from books_online.products.model import Product
from books_online.products.service import add_product, get_all, get_product_by_id
from books_online.auth.utils import get_token_user, is_token_valid, is_token_user_admin

router = APIRouter()

@router.get("/products/all")
async def get_products(request: Request):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    return {"products": get_all()}

@router.get("/products/{product_id}")
async def get_product(request: Request, product_id: int):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    return {"product": get_product_by_id(product_id)}

@router.post("/products/add")
async def add_product_endpoint(request: Request, data: dict):
    if not is_token_user_admin(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    product = Product(name=data.get("name"), description=data.get("description"), price=data.get("price"), inventory=data.get("inventory"))
    product = add_product(product)
    return {"message": "Product created successfully", "product_id": product.id}
