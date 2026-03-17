# In-memory storage for demonstration
orders_db = []

def create_order(order_data: dict):
    """Add order to the in-memory list"""
    orders_db.append(order_data)

def get_all_orders():
    """Return all orders"""
    return orders_db