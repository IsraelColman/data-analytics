# Israel Colman
# 11/13/2026

a = 80
b = 100.1
c = 100

if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

print(f'The smallest number is {smallest}')
print(f'The largest number is {largest}')