from fastapi import APIRouter
from app.schemas import Invoice
from app.services import create_pdf

router = APIRouter()

@router.post("/")
async def get_invoices_info(info: Invoice):
    create_pdf(info)
    return {
        "customer": info.customer.customer_name,
        "customer_email": info.customer.customer_email,
        "items": info.items
    }