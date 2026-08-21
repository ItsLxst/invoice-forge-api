from fastapi import APIRouter
from app.schemas import Invoice

router = APIRouter()

@router.post("/")
async def get_invoices_info(info: Invoice):
    return {"message": "Hello World"}