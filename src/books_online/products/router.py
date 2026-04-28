

from fastapi import APIRouter, Request
from books_online.products.model import Product
from books_online.products.service import add_product, get_all, get_product_by_id, add_product_inventory
from books_online.auth.utils import get_token_user, is_token_valid, is_token_user_admin

router = APIRouter()

@router.get("/products/all")
async def get_products(request: Request):
    return {"products": get_all()}

@router.get("/products/{product_id}")
async def get_product(request: Request, product_id: int):
    return {"product": get_product_by_id(product_id)}

@router.post("/products/add")
async def add_product_endpoint(request: Request, data: dict):
    product = Product(name=data.get("name"), description=data.get("description"), price=data.get("price"), inventory=data.get("inventory"))
    product = add_product(product)
    return {"message": "Product created successfully", "product_id": product.id}

@router.post("/products/add_inventory")
async def add_inventory_to_product(request: Request, data: dict):
    product = get_product_by_id(data.get("product_id")) # type: ignore
    if not product:
        return {"error": "Product not found"}
    quantity = data.get("quantity")
    add_product_inventory(product.id, quantity) # type: ignore
    return {"message": "Inventory added to products successfully for product " + str(product.id)}
