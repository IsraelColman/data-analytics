# Description: Using if, elif, and else
# Author: Israel Colman

department_code = int(input('Enter department code: '))

if department_code == 1:
    print(f'Department name: Marketing')
elif department_code == 5:
    print(f'Department name: Human Resources')
elif department_code == 10:
    print(f'Department name: Accounting')
elif department_code == 12:
    print(f'Department name: Legal')
elif department_code == 18:
    print(f'Department name: IT')
elif department_code == 20:
    print(f'Department name: Customer Relations')
else:
    print(f'Department not found')