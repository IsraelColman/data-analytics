# Description: Understanding if statements
# Author: Israel Colman

x = 100
y = 20

# a)
if x / y == 5:
    print(f'x divided by y is 5')
    x = 1
else:
    print(f'are the variables set up correctly?')


# b)
if x * y == y:
    print(f'now x times y is y')
    x = x*2
else:
    print(f'Whoops, x equals {x}')


# c)
if x < y:
    print(f'x is less than y')
    x = x*2
else:
    print(f'uh oh, x is not less than y')


# d)
if x > y:
    print(f'how is x greater than y??')
else:
    print(f'x is NOT greater than y')

print(f'the final value of x is {x} and the final value of y is {y}')