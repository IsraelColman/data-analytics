# Israel Colman
# taxes.py
# 11/10/2026

# How much is taxes is withheld from salary every month?
monthly_salary = float(input("What is your monthly salary?: "))
federal_tax_rate = 0.23

tax_withheld = monthly_salary * federal_tax_rate

print(f'Monthly salary is ${monthly_salary:,}, the federal tax rate is {federal_tax_rate}. the tax withheld is ${round(tax_withheld, 2)}')