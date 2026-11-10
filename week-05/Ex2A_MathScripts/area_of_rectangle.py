# Israel Colman
# area_of_rectangle.py
# 11/10/2026


# Calculating the area of a rectangle
length = input("what is the length of the first side?: 30")
width = input("what is the length of the second side?: 4")

area = length * width

print(f'Side A is {length}')
print(f'Side B is {width}')
print(f'The area of the rectangle is {area}')


# when i added the input function to the length and width variables,\
# it caused an error because the input function returns a string,\
# and you cannot multiply two strings together. I would have to use int function\
# to convert the input values to integers before the muliplication.