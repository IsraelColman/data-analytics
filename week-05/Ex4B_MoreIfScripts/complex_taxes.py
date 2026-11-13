# Israel Colman
# 11/13/2026

pay_rate = float(input('Enter your pay rate: '))
hours_worked = float(input('Enter your hours worked: '))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = pay_rate * hours_worked

#print(f'Gross pay: {gross_pay:.2f}')

annual_gross_pay = gross_pay * 52
#print(annual_gross_pay)

filing_status = input('Enter filing status (single or joint): ')

if filing_status == 'single':
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross_pay < 12000:
        tax_rate = 0.0
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print(f'Invalid filing status')


tax_witheld = gross_pay * tax_rate
net_pay = gross_pay - tax_witheld

print()
print(f'You worked {hours_worked} hours this period')
print(f'Because you earned ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:,.2f}')
print(f'Your filing status is {filing_status}')
print(f'Your tax witholding for the week is ${tax_witheld:.2f}')
print(f'Your net pay is ${net_pay:,.2f}')