from pydantic import BaseModel, Field, field_validator, field_serializer

class Order(BaseModel):
    orderId: int = Field(..., description="Unique identifier for the order", gt=0)
    customerId: int = Field(..., description="Unique identifier for the customer", gt=0)
    amount: float = Field(..., description="Total amount of the order", gt=0)
    customer_type: str = Field("regular", description="Type of customer (e.g., regular, premium)")
    card_type: int