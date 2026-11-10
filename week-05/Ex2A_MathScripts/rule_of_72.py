# Israel Colman
# rule_of_72.py
# 11/10/2026

# Calculating the rule of 72
savings_account = 10000
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
future_value = savings_account * 2

print(f'Your current savings is ${savings_account:,.2f}.\
 At a {format(interest_rate, ".0%")} interest rate, your savings account will be worth\
 ${future_value:,.2f} in {format(years_to_double, ".1f")} years.')