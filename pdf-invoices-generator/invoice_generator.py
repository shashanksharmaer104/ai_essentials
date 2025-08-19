from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

class InvoiceGenerator:
    def __init__(self):
        self.width, self.height = A4
        
    def generate_invoice(self, filename="invoice_august_2025.pdf"):
        c = canvas.Canvas(filename, pagesize=A4)
        
        # Header
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, self.height - 50, "AIRTEL INDIA LIMITED")
        c.setFont("Helvetica", 10)
        c.drawString(50, self.height - 70, "GSTIN: 07AAACA3633M1Z3")
        c.drawString(50, self.height - 85, "Address: Bharti Crescent, 1 Nelson Mandela Road, Vasant Kunj, New Delhi - 110070")
        
        # Invoice Details
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, self.height - 120, "INVOICE")
        c.setFont("Helvetica", 10)
        c.drawString(50, self.height - 140, f"Invoice No: INV-AUG-2025-001")
        c.drawString(50, self.height - 155, f"Date: 01-Aug-2025")
        c.drawString(50, self.height - 170, f"Due Date: 31-Aug-2025")
        
        # Customer Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, self.height - 200, "Bill To:")
        c.setFont("Helvetica", 10)
        c.drawString(50, self.height - 220, "Customer Name: Rajesh Kumar")
        c.drawString(50, self.height - 235, "Mobile: +91-9876543210")
        c.drawString(50, self.height - 250, "Address: 123, MG Road, Bangalore - 560001")
        c.drawString(50, self.height - 265, "Customer ID: AIR123456789")
        
        # Service Details Table
        y_pos = self.height - 320
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y_pos, "Description")
        c.drawString(300, y_pos, "Amount (₹)")
        
        c.line(50, y_pos - 5, 500, y_pos - 5)
        
        y_pos -= 25
        c.setFont("Helvetica", 10)
        c.drawString(50, y_pos, "Broadband Service - August 2025")
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
        c.drawString(50, y_pos, "Bank: HDFC Bank")
        y_pos -= 15
        c.drawString(50, y_pos, "Account No: 50200012345678")
        y_pos -= 15
        c.drawString(50, y_pos, "IFSC: HDFC0001234")
        
        # Footer
        c.setFont("Helvetica", 8)
        c.drawString(50, 50, "This is a computer generated invoice. No signature required.")
        
        c.save()
        return filename

if __name__ == "__main__":
    generator = InvoiceGenerator()
    filename = generator.generate_invoice()
    print(f"Invoice generated: {filename}")