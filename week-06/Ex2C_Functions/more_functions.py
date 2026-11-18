# Israel Colman
# 11/17/2026

# Mailing address function
def display_mailing_label(name, address, city, state, zip):
    return f'{name}\n{address}\n{city}, {state} {zip}'

print(display_mailing_label('John Doe', '240 W 500 S', 'Salt Lake City', 'UT', '84101'))
print()


# Adding numbers with a function
def add_numbers(*numbers):
    total = sum(numbers)

    expression = ''
    for i in range(len(numbers)):
        expression += str(numbers[i])

        if i < len(numbers) - 1:
            expression += ' + '
    print(f'{expression} = {total}')


add_numbers(12, 55, 24, 42, 6, 18)


# Calculate change due and remaining balance
def display_receipt(total_due, amount_paid):
    if amount_paid > total_due:
        change_due = amount_paid - total_due
        print(f'Total Due: ${total_due:,.2f}\nAmount Paid: ${amount_paid:,.2f}\n\nChange Due: ${change_due:,.2f}')
    else:
        remaining_balance = total_due - amount_paid
        print(f'Total Due: ${total_due:,.2f}\nAmount Paid: ${amount_paid:,.2f}\n\nRemaining Balance: ${remaining_balance:,.2f}')
    

print()
display_receipt(
    float(input('Enter Total Due: ')),
    float(input('Enter Amount Paid: '))
)