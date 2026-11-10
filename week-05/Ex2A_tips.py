# Israel Colman
# Ex2A_tips.py
# Lab 1
# 11/11/2026


# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
#print("The total due is " + str(total_due))


# Why is the string function being used? we are converting the data type of the variable total_due into a string.\
# the reason is because you cannot concatenate a string and a float together.\
# so we convert the float into a string so that it can be concatenated with the other string.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Total due is " + str(total_due))

print("Tip is " + format(tip, ".2f"))