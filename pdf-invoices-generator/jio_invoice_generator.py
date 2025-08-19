from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
from reportlab.lib.utils import ImageReader

class JioInvoiceGenerator:
    def __init__(self):
        self.width, self.height = A4
        
    def generate_invoice(self, filename="jio_invoice_august_2025.pdf"):
        c = canvas.Canvas(filename, pagesize=A4)
        
        # Logo
        try:
            c.drawImage("jiofiber-logo.jpg", 50, self.height - 80, width=100, height=40)
        except:
            pass
        
        # Header
        c.setFont("Helvetica-Bold", 16)
        c.drawString(160, self.height - 50, "RELIANCE JIO INFOCOMM LIMITED")
        c.setFont("Helvetica", 10)
        c.drawString(160, self.height - 70, "GSTIN: 27AAACR5055K1Z7")
        c.drawString(50, self.height - 100, "Address: Reliance Corporate Park, Thane-Belapur Road, Navi Mumbai - 400701")
        
        # Invoice Details
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, self.height - 135, "INVOICE")
        c.setFont("Helvetica", 10)
        c.drawString(50, self.height - 155, f"Invoice No: JIO-AUG-2025-001")
        c.drawString(50, self.height - 170, f"Date: 01-Aug-2025")
        c.drawString(50, self.height - 185, f"Due Date: 31-Aug-2025")
        
        # Customer Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, self.height - 215, "Bill To:")
        c.setFont("Helvetica", 10)
        c.drawString(50, self.height - 235, "Customer Name: Priya Sharma")
        c.drawString(50, self.height - 250, "Mobile: +91-9123456789")
        c.drawString(50, self.height - 265, "Address: 456, Park Street, Mumbai - 400001")
        c.drawString(50, self.height - 280, "Customer ID: JIO987654321")
        
        # Service Details Table
        y_pos = self.height - 335
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y_pos, "Description")
        c.drawString(300, y_pos, "Amount (₹)")
        
        c.line(50, y_pos - 5, 500, y_pos - 5)
        
        y_pos -= 25
        c.setFont("Helvetica", 10)
        c.drawString(50, y_pos, "JioFiber Broadband - August 2025")
        c.drawString(300, y_pos, "1,017.00")
        
        y_pos -= 20
        c.drawString(50, y_pos, "CGST @ 9%")
        c.drawString(300, y_pos, "91.53")
        
        y_pos -= 20
        c.drawString(50, y_pos, "SGST @ 9%")
        c.drawString(300, y_pos, "91.53")
        
        c.line(50, y_pos - 10, 500, y_pos - 10)
        
        y_pos -= 25
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y_pos, "Total Amount")
        c.drawString(300, y_pos, "₹ 1,200.00")
        
        # Payment Details
        y_pos -= 50
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y_pos, "Payment Details:")
        c.setFont("Helvetica", 9)
        y_pos -= 20
        c.drawString(50, y_pos, "Bank: ICICI Bank")
        y_pos -= 15
        c.drawString(50, y_pos, "Account No: 60300087654321")
        y_pos -= 15
        c.drawString(50, y_pos, "IFSC: ICIC0006030")
        
        # Footer
        c.setFont("Helvetica", 8)
        c.drawString(50, 50, "This is a computer generated invoice. No signature required.")
        
        c.save()
        return filename

if __name__ == "__main__":
    generator = JioInvoiceGenerator()
    filename = generator.generate_invoice()
    print(f"Jio invoice generated: {filename}")