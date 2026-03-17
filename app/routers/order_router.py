from fastapi import APIRouter
from app.services.order_service import create_order, get_all_orders
from pydantic import BaseModel
from app.models.order_model import Order
from app.exceptions.user_exceptions import UserNotFoundError
from fastapi import APIRouter, Depends
from app.routers.auth2_router import verify_token

# Router with prefix
router = APIRouter(prefix="/orders", tags=["Orders"])


# @router.get("/")
# def get_orders(user=Depends(verify_token)):

#     return {
#         "message": f"Hello {user}, these are your orders"
#     }


# POST endpoint to submit order
@router.post("/", summary="Submit a new order")
def submit_order(order: Order):
    create_order(order.dict())
    return {"message": "Order submitted successfully11111", "orderId": order.orderId}

# GET endpoint to list all orders
@router.get("/", summary="Get all orders")
def list_orders(user=Depends(verify_token)):
    return get_all_orders()

@router.get("/{order_id}")
def get_order(order_id: int):
    order_list = get_all_orders()
    order = next((o for o in order_list if o['orderId'] == order_id), None)

    if order:
        return order
    raise UserNotFoundError(order_id)