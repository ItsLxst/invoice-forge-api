from reportlab.pdfgen import canvas
from app.schemas import Invoice
import uuid # create unique id (Universally Unique Identifier)


def create_pdf(info: Invoice):
    filename = f"invoice_{uuid.uuid4()}.pdf"
    invoice_pdf = canvas.Canvas(filename)

    # title
    invoice_pdf.setFont("Helvetica-Bold", 24)
    invoice_pdf.drawString(250, 750, "INVOICE")

    # customer info
    invoice_pdf.setFont("Helvetica", 12)
    invoice_pdf.drawString(100, 700, f"Customer: {info.customer.customer_name}")
    invoice_pdf.drawString(100, 680, f"Email: {info.customer.customer_email}")

    # table headers
    invoice_pdf.setFont("Helvetica-Bold", 11)
    invoice_pdf.drawString(100, 630, "Product")
    invoice_pdf.drawString(350, 630, "Quantity")
    invoice_pdf.drawString(450, 630, "Price")

    # invoice items
    invoice_pdf.setFont("Helvetica", 11)

    y = 605
    total = 0

    for item in info.items:
        item_total = item.quantity * item.price
        total += item_total

        invoice_pdf.drawString(100, y, item.name)
        invoice_pdf.drawString(350, y, str(item.quantity))
        invoice_pdf.drawString(450, y, f"${item.price:.2f}")

        y -= 25

    # total
    invoice_pdf.setFont("Helvetica-Bold", 12)
    invoice_pdf.drawString(350, y - 10, f"Total: ${total:.2f}")

    invoice_pdf.showPage()
    invoice_pdf.save()
    return filename