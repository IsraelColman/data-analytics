# Israel Colman
# 11/14/2026

balance = 0
savings_goal = 10000
weekly_savings = 1000
treat_purchased = False

while True:
    balance += weekly_savings
    print(f'This week my balance increased to ${balance:,.2f}')

    if balance > savings_goal / 2:
        print(f'Almost there! This week my balance is ${balance:,.2f}')

    if balance >= savings_goal * 0.75 and not treat_purchased:
        balance -= 500
        treat_purchased = True
        print(f'So close! After treating myself, my balance is up to ${balance:,.2f}')

    if balance >= savings_goal:
        break

print(f'Goal met! My current balance is ${balance:,.2f}')