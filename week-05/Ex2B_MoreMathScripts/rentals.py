# Israel Colman
# rentals.py
# 11/10/2026

# Van rentals
import math

tourists = int(input("How many tourists are there?: "))

vans_needed = math.ceil(tourists / 15)
rental_cost = vans_needed * 250
cost_per_person = rental_cost / tourists

van_cost = vans_needed * 250
collected = tourists * cost_per_person
leftover = collected - van_cost

print(f"Tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total rental cost: ${rental_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

print(f'The charge per person is: ${cost_per_person:.2f}')
print(f'I collected: ${collected:.2f}')
print(f'The cost of the vans were ${van_cost:.2f}')
print(f'My left over money is ${leftover:.2f}')