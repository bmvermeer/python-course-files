from fpdf import FPDF

class Bill:
    """
    Object Bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(unit='pt')
        pdf.add_page()

        pdf.set_font('Arial', 'B', 24)

        #Icon
        pdf.image("files/house.png", w=30, h=30)

        # Title
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        # Value
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(w=0, h=40, txt="Period: "+ bill.period, border=1, ln=1)

        pdf.set_font(family='Arial', size=12, style='B')
        # Header
        pdf.cell(w=300, h=20, txt='Name:', border=1)
        pdf.cell(w=0, h=20, txt='Amount', border=1, ln=1)

        pdf.set_font(family='Arial', size=12)
        # flatmate1
        pdf.cell(w=300, h=20, txt=flatmate1.name, border=1)
        pdf.cell(w=0, h=20, txt=str(round(flatmate1.pays(bill, flatmate2),2)), border=1, ln=1)

        # flatmate1
        pdf.cell(w=300, h=20, txt=flatmate2.name, border=1)
        pdf.cell(w=0, h=20, txt=str(round(flatmate2.pays(bill, flatmate1),2)), border=1, ln=1)

        pdf.output(self.filename)


bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.pays(bill, marry))
print(marry.pays(bill, john))

pdf = PdfReport('bill-'+bill.period+'.pdf')
pdf.generate(john, marry, bill)
