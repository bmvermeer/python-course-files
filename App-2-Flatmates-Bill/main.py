import os.path
import webbrowser

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
        webbrowser.open('file://' + os.path.realpath(self.filename))


amount = float(input("Hello what is the bill amount?"))
period = input("What is the period of the bill e.g. April 2021")
print("The amount is:", amount)
print("The period is:", period)

person1Name = input("What is your name?")
person1Days = int(input("How many days where you in house?"))

person2Name = input("What is your flatmates name?")
person2Days = int(input("How many days was this person in house?"))

bill = Bill(amount=amount, period=period)
you = Flatmate(name=person1Name, days_in_house=person1Days)
flatmate = Flatmate(name=person2Name, days_in_house=person2Days)

print(f"{you.name} pays:", you.pays(bill, flatmate))
print(f"{flatmate.name} pays:", flatmate.pays(bill, you))

pdf = PdfReport('bill-'+bill.period+'.pdf')
pdf.generate(you, flatmate, bill)
