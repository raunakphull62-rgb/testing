python
from pydantic import BaseModel
from typing import Optional

# Define a model for users
class User(BaseModel):
    id: str
    email: str
    password: str
    name: Optional[str]

# Define a model for products
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float

# Define a model for orders
class Order(BaseModel):
    id: str
    user_id: str
    product_id: str
    quantity: int
    total: float