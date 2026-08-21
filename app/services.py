from reportlab.pdfgen import canvas
from app.schemas import Invoice

def create_pdf(info: Invoice):
    empty_canvas = canvas.Canvas("invoice.pdf")

    empty_canvas.drawString(100, 780, info.customer.customer_name)
    empty_canvas.drawString(100, 765, info.customer.customer_email)

    x = 100
    y = 750
    for item in info.items:
        item_text = f"{item.name} | Quantity: {item.quantity} | Price: {item.price}"
        empty_canvas.drawString(x, y, item_text)
        y -= 15

    empty_canvas.showPage()
    empty_canvas.save()