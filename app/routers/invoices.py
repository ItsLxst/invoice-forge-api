from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas import Invoice
from app.services import create_pdf
from fastapi import Depends
from app.auth import verify_api_key

router = APIRouter()

@router.post("/", dependencies=[Depends(verify_api_key)])
async def get_invoices_info(info: Invoice):
    filename = create_pdf(info)
    return FileResponse(filename)