from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas import Invoice
from app.services import create_pdf

router = APIRouter()

@router.post("/")
async def get_invoices_info(info: Invoice):
    create_pdf(info)
    return FileResponse("invoice.pdf")