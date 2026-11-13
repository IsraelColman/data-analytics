# Description: Calculate gross pay
# Author: Israel Colman

pay_rate = float(input('Enter your pay rate: '))
hours_worked = float(input('Enter your hours worked: '))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = pay_rate * hours_worked

print(f'Gross pay: {gross_pay:.2f}')