from pydantic import BaseModel

class Customer(BaseModel):
    customer_name: str
    customer_email: str

class Item(BaseModel):
    name: str
    quantity: int
    price: float

class Invoice(BaseModel):
    customer: Customer
    items: list[Item]