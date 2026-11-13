# Description: Using the match/case statement
# Author: Israel Colman

department_name = int(input('Enter department number: '))

match department_name:
    case 1:
        print(f'Department name: Marketing')
    case 5:
        print(f'Department name: Human Resources')
    case 10:
        print(f'Department name: Accounting')
    case 12:
        print(f'Department name: Legal')
    case 18:
        print(f'Department name: IT')
    case 20:
        print(f'Department name: Customer Relations')
    case _:
        print(f'Department not found')