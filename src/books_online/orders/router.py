from fastapi import APIRouter, Request
import datetime
from books_online.auth.model import User
from books_online.auth.utils import get_token_user, is_token_valid, is_token_user_admin
from books_online.orders.model import Order, OrderLine
from books_online.products.model import Product
from books_online.orders.service import create_new_order, create_order_line, get_all_orders, get_orders_by_user_id, get_order_by_id, get_first_status
from books_online.products.service import get_product_by_id
router = APIRouter()

@router.post("/orders/new")
async def new_order(request: Request):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    user = get_token_user(request.headers.get("Authorization", ""))
    first_status = get_first_status() # type: ignore
    if not is_token_user_admin(request.headers.get("Authorization", "")):
        order = Order(created_at=datetime.datetime.now(), status_id=first_status.id, user_id=user['user'].id) # type: ignore
        new_order = create_new_order(order)
    else:
        return {"error": "Admin Users cannot create orders"}
    return {"message": "Order created successfully", "order_id": new_order.id}

@router.get("/orders/all")
async def get_orders(request: Request):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    user = get_token_user(request.headers.get("Authorization", ""))
    if is_token_user_admin(request.headers.get("Authorization", "")):
        orders = get_all_orders()
    else:
        orders = get_orders_by_user_id(user['user'].id) # type: ignore
    return {"orders": orders}

@router.get("/orders/{order_id}")
async def get_order(request: Request, order_id: int):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    order = get_order_by_id(order_id)
    if not order:
        return {"error": "Order not found"}
    return {"order": order}

@router.post("/orders/{order_id}/add_product")
async def add_product_to_order(request: Request, order_id: int, data: dict):
    if not is_token_valid(request.headers.get("Authorization", "")):
        return {"error": "Unauthorized"}
    order = get_order_by_id(order_id)
    if not order:
        return {"error": "Order not found"}
    product = get_product_by_id(data.get("product_id")) # type: ignore
    if not product:
        return {"error": "Product not found"}
    # if product.inventory < data.get("quantity"):
    #     return {"error": "Not enough inventory"}
    # product.inventory -= data.get("quantity")
    # order_line = OrderLine(product_id=product.id, quantity=data.get("quantity"), subtotal=product.price * data.get("quantity"), order_id=order.id)
    # new_order_line = create_order_line(order_line)
    # return {"message": "Product added to order successfully", "order_line_id": new_order_line.id}
    return True
