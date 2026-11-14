# Israel Colman
# 11/14/2026

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

total_sales = 0

for name, region, price in sales_data:
    print(f'{name} ({region}): ${price:,.2f}')

    if price > 5000:
            print(f'^ Top Performer')

    total_sales += price

print(f'Total Sales: ${total_sales:,.2f}')