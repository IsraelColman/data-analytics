# Israel Colman
# 11/17/2026

import random

products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 
    'Webcam', 'Headset', 'Docking Station', 
    'USB Hub', 'Desk Lamp', 'Surge Protector'
]

print('\n------------------------------------------------------')

prod_of_day = random.choice(products)
print(f'Product of the day: {prod_of_day}')

prod_survey = random.sample(products, 3)
print(f'Products for survey: {prod_survey}')

prod_shuffled = random.shuffle(products)
print(f'Shuffled products: {products}')

randint = random.randint(50, 300)
print(f'Transaction count: {randint}')

print('-' * 54)