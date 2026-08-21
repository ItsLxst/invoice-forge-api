from fastapi import APIRouter
from app.schemas import Invoice

router = APIRouter()

@router.post("/")
async def get_invoices_info(info: Invoice):
    return {
        "customer": info.customer.customer_name,
        "customer_email": info.customer.customer_email,
        "items": info.items
    }