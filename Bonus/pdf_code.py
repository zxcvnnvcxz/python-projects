from fpdf import FPDF

FILEPATH = "../Files"

class Receipt:
    def __init__(self, article_id, article_name, article_price):
        self.article_id = article_id
        self.article_name = article_name
        self.article_price = article_price

    def generateReceipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        receipt_item_nr = self.article_id
        receipt_item_name: str = self.article_name.title()
        receipt_item_price = self.article_price

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt Item nr.{receipt_item_nr}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {receipt_item_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {receipt_item_price}", ln=1)

        pdf.output(f"{FILEPATH}/receipt.pdf")